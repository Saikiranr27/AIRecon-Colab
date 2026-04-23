"""Tests for ollama.py — client init, capabilities, complete, and utility methods."""

from __future__ import annotations

import asyncio
from unittest.mock import MagicMock, patch

import pytest


class TestOllamaClientInit:
    def test_init_reads_config(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = True
            cfg.ollama_supports_native_tools = False
            mock_cfg.return_value = cfg

            client = OllamaClient()
            assert client._host == "http://localhost:11434"
            assert client.model == "llama3"

    def test_init_overrides_url_and_model(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            mock_cfg.return_value = cfg

            client = OllamaClient(base_url="http://other:11434", model="mistral")
            assert client._host == "http://other:11434"
            assert client.model == "mistral"

    def test_init_forces_native_tools_off_when_thinking_off(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = True
            mock_cfg.return_value = cfg

            client = OllamaClient()
            assert client._supports_native_tools is False


class TestDetectModelCapabilities:
    def test_detects_thinking_from_capabilities(self):
        from airecon.proxy.ollama import _detect_model_capabilities_from_show

        thinking, native_tools = _detect_model_capabilities_from_show(
            "llama3", {"capabilities": ["thinking", "tools"]}
        )
        assert thinking is True
        assert native_tools is True

    def test_detects_thinking_from_template(self):
        from airecon.proxy.ollama import _detect_model_capabilities_from_show

        thinking, _ = _detect_model_capabilities_from_show(
            "deepseek",
            {"capabilities": [], "template": "<think>\n{{ .Prompt }}\n</think>"},
        )
        assert thinking is True

    def test_native_tools_requires_thinking(self):
        from airecon.proxy.ollama import _detect_model_capabilities_from_show

        thinking, native_tools = _detect_model_capabilities_from_show(
            "llama3", {"capabilities": ["tools"]}
        )
        assert thinking is False
        assert native_tools is False

    def test_empty_response(self):
        from airecon.proxy.ollama import _detect_model_capabilities_from_show

        thinking, native_tools = _detect_model_capabilities_from_show("model", {})
        assert thinking is False
        assert native_tools is False


class TestOllamaComplete:
    @pytest.fixture
    def client(self):
        from airecon.proxy.ollama import OllamaClient

        with (
            patch("airecon.proxy.ollama.get_config") as mock_cfg,
            patch("airecon.proxy.ollama.get_memory_manager") as mock_memory,
        ):
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            cfg.ollama_timeout = 120.0
            cfg.ollama_chunk_timeout = 60.0
            mock_cfg.return_value = cfg
            mock_memory.return_value = MagicMock()

            c = OllamaClient()
            c._httpx_client = MagicMock()
            c._initialized = True
            c._memory_manager_mock = mock_memory.return_value
            yield c

    @pytest.mark.asyncio
    async def test_complete_returns_content(self, client):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "message": {"content": "Hello world", "role": "assistant"}
        }
        with patch.object(client, "_run_http_request", return_value=mock_resp):
            result = await client.complete(messages=[{"role": "user", "content": "hi"}])
        assert result == "Hello world"

    @pytest.mark.asyncio
    async def test_complete_retries_on_none_response(self, client):
        with patch.object(client, "_run_http_request", return_value=None):
            with pytest.raises(RuntimeError, match="None response"):
                await client.complete(
                    messages=[{"role": "user", "content": "hi"}], max_retries=1
                )

    @pytest.mark.asyncio
    async def test_complete_retries_on_timeout(self, client):
        import asyncio

        async def raise_timeout(*args, **kwargs):
            raise asyncio.TimeoutError()

        with patch.object(client, "_run_http_request", side_effect=raise_timeout):
            with pytest.raises(RuntimeError, match="timeout"):
                await client.complete(
                    messages=[{"role": "user", "content": "hi"}], max_retries=1
                )

    @pytest.mark.asyncio
    async def test_complete_raises_on_invalid_response_format(self, client):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"unexpected_key": "value"}
        with patch.object(client, "_run_http_request", return_value=mock_resp):
            with pytest.raises(RuntimeError, match="Invalid Ollama response format"):
                await client.complete(
                    messages=[{"role": "user", "content": "hi"}], max_retries=0
                )

    @pytest.mark.asyncio
    async def test_complete_records_model_performance(self, client):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "message": {"content": "Hello world", "role": "assistant"}
        }

        with patch.object(client, "_run_http_request", return_value=mock_resp):
            await client.complete(
                messages=[{"role": "user", "content": "hi"}],
                max_retries=0,
                operation="analysis",
            )

        kwargs = client._memory_manager_mock.record_model_performance.call_args.kwargs
        assert kwargs["model_name"] == "llama3"
        assert kwargs["task_type"] == "analysis"
        assert kwargs["success"] is True

    @pytest.mark.asyncio
    async def test_chat_stream_records_model_performance(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            cfg.ollama_timeout = 120.0
            cfg.ollama_chunk_timeout = 60.0
            mock_cfg.return_value = cfg
            client = OllamaClient()

        class _FakeStreamResponse:
            def raise_for_status(self):
                return None

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                return False

            async def aiter_lines(self):
                for line in [
                    '{"message":{"content":"hello"},"done":false}',
                    '{"message":{"content":""},"done":true}',
                ]:
                    yield line

        class _FakeHttpClient:
            def stream(self, *args, **kwargs):
                return _FakeStreamResponse()

        memory = MagicMock()
        client._request_semaphore = asyncio.Semaphore(1)

        with patch("airecon.proxy.ollama.get_memory_manager", return_value=memory):
            from airecon.proxy.ollama import OllamaClient as OllamaClass

            old_httpx_client = OllamaClass._httpx_client
            try:
                OllamaClass._httpx_client = _FakeHttpClient()
                chunks = [
                    chunk
                    async for chunk in client.chat_stream(
                        messages=[{"role": "user", "content": "ping"}],
                        max_retries=0,
                        operation="recon",
                    )
                ]
            finally:
                OllamaClass._httpx_client = old_httpx_client

        assert len(chunks) == 2
        kwargs = memory.record_model_performance.call_args.kwargs
        assert kwargs["task_type"] == "recon"
        assert kwargs["success"] is True


class TestOllamaResetContext:
    @pytest.fixture
    def client(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            cfg.ollama_timeout = 120.0
            cfg.ollama_chunk_timeout = 60.0
            mock_cfg.return_value = cfg

            c = OllamaClient()
            c._httpx_client = MagicMock()
            c._initialized = True
            return c

    @pytest.mark.asyncio
    async def test_reset_context_returns_true_on_success(self, client):
        with patch.object(client, "_run_http_request", return_value=MagicMock()):
            result = await client.reset_context()
        assert result is True

    @pytest.mark.asyncio
    async def test_reset_context_returns_false_on_timeout(self, client):
        import asyncio

        async def raise_timeout(*args, **kwargs):
            raise asyncio.TimeoutError()

        with patch.object(client, "_run_http_request", side_effect=raise_timeout):
            result = await client.reset_context()
        assert result is False

    @pytest.mark.asyncio
    async def test_reset_context_returns_false_on_http_error(self, client):
        import httpx

        async def raise_http_error(*args, **kwargs):
            raise httpx.HTTPError("server error")

        with patch.object(client, "_run_http_request", side_effect=raise_http_error):
            result = await client.reset_context()
        assert result is False


class TestOllamaUnloadModel:
    @pytest.fixture
    def client(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            mock_cfg.return_value = cfg

            c = OllamaClient()
            c._httpx_client = MagicMock()
            c._initialized = True
            return c

    @pytest.mark.asyncio
    async def test_unload_model_succeeds(self, client):
        with patch.object(client, "_run_http_request", return_value=MagicMock()):
            await client.unload_model()

    @pytest.mark.asyncio
    async def test_unload_model_logs_error_on_failure(self, client):
        async def raise_error(*args, **kwargs):
            raise RuntimeError("failed")

        with patch.object(client, "_run_http_request", side_effect=raise_error):
            await client.unload_model()


class TestDynamicTimeout:
    def test_compression_gets_longer_timeout(self):
        from airecon.proxy.ollama import OllamaClient

        with patch("airecon.proxy.ollama.get_config") as mock_cfg:
            cfg = MagicMock()
            cfg.ollama_url = "http://localhost:11434"
            cfg.ollama_model = "llama3"
            cfg.ollama_supports_thinking = False
            cfg.ollama_supports_native_tools = False
            cfg.ollama_chunk_timeout = 60.0
            mock_cfg.return_value = cfg

            c = OllamaClient()
            assert c._get_dynamic_timeout("compression") >= 180.0
            assert c._get_dynamic_timeout("inference") == 60.0
