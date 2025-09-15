"""Test configuration and fixtures for pydantic-ai-stash."""

import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest
from pydantic_ai.messages import BinaryContent

from pydantic_ai_stash.adapters import FSAdapter


@pytest.fixture
def temp_storage_dir() -> Iterator[Path]:
    """Provide a clean directory for testing storage."""
    # Use a unique temporary directory for each test
    with tempfile.TemporaryDirectory(prefix="pydantic_ai_stash_test_") as temp_dir:
        storage_dir = Path(temp_dir)
        yield storage_dir
        # Cleanup happens automatically when context manager exits


@pytest.fixture
def fs_adapter(temp_storage_dir: Path) -> FSAdapter:
    """Provide a filesystem adapter for testing."""
    return FSAdapter(str(temp_storage_dir))


@pytest.fixture
def sample_image_binary() -> BinaryContent:
    """Provide sample image binary content for testing."""
    return BinaryContent(
        data=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01",
        media_type="image/png",
    )


@pytest.fixture
def sample_audio_binary() -> BinaryContent:
    """Provide sample audio binary content for testing."""
    return BinaryContent(data=b"RIFF\x24\x00\x00\x00WAVE", media_type="audio/wav")


@pytest.fixture
def sample_video_binary() -> BinaryContent:
    """Provide sample video binary content for testing."""
    return BinaryContent(data=b"\x00\x00\x00\x20ftypmp41", media_type="video/mp4")


@pytest.fixture
def sample_document_binary() -> BinaryContent:
    """Provide sample document binary content for testing."""
    return BinaryContent(data=b"%PDF-1.4\n1 0 obj", media_type="application/pdf")


@pytest.fixture
def sample_binary_with_metadata() -> BinaryContent:
    """Provide binary content with metadata for testing."""
    return BinaryContent(
        data=b"test content",
        media_type="image/jpeg",
        identifier="test-image-123",
        vendor_metadata={"source": "test", "quality": "high"},
    )
