# Pydantic AI Stash (prerelease)

Efficient serialization and storage for Pydantic AI conversations with binary content.

## Overview

Pydantic AI Stash provides a clean, maintainable library for handling binary content within Pydantic AI message structures. It enables efficient storage and retrieval of binary data (images, audio, documents, etc.) while preserving metadata and ensuring round-trip fidelity.

Currently, we just have a simplistic file store adapter wired up. An adapter is designed specifically to hold your custom business logic (deduping, expiration times, db, s3, id, etc.)

## Key Features

- **Flexible Adapter Layer**: A basic adapter class handles the identification, stashing, and loading of content types. Plug in your DB, S3, etc. tools here. 
- **Type Safety**: Full type hints and compatibility with Pydantic AI message formats
- **Metadata Preservation**: Maintains all original BinaryContent metadata during stash/load cycles
- **Nested Content Support**: Handles BinaryContent in nested message part content lists
- **Storage Abstraction**: Pluggable storage adapters (filesystem included, extensible for cloud storage)
- **Error Handling**: Robust error handling for storage operations

## Quick Start

```python
from pydantic_ai_stash import BinaryStash, FSAdapter

# Set up storage
storage = FSAdapter("./binary_storage")
stash = BinaryStash(storage)

# Stash binary content in messages
stashed_messages = stash.stash_binaries_in_messages(messages)

# Later, load binary content back
loaded_messages = stash.load_binaries_in_messages(stashed_messages)
```

## Installation

```bash
pip install pydantic-ai-stash
```

## License

MIT License - see LICENSE file for details.
