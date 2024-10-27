<img src = "https://static.itch.io/images/itchio-textless-white.svg" alt="Itchio Logo" align="right" width="200"/>

# Panda3D Itch.io

This Python module adds Itchio Launcher support to the Panda3D game engine, enabling user authentication,
ownership verification, and purchase verification inside your Panda3D application.

This module requires your game to be downloaded and ran through the official Itch.io launcher application
to function as intended.

## Features

- Integrate Itchio Launcher with Panda3D
- Allows games to verify they were launched from the launcher.
- Allows games to retrieve the details of the user playing.
- Allows games to retrieve information about the user's games and purchases.

## Installation

```bash
pip install panda3d-itchio
```

## Usage

```python
from panda3d_itchio import launcher
import sys

# Exit if we have not been correctly launched.
launcher_launched = launcher.verify_launched_from_itchio()
if launcher_launched == False:
    sys.exit(2)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
