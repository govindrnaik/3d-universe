# 3D Universe

A web-based interactive 3D visualization platform for exploring cosmic phenomena and space missions.

## Features

- **Solar System Visualization**: Interactive 3D model of our solar system with planets and their orbits
- **Big Bang**: Visual representation of the beginning of our universe
- **Black Hole**: Interactive 3D visualization of a black hole and its effects
- **Space Missions**:
  - Voyager Mission
  - Starlink Network
  - Chandrayaan Mission
  - Mangalyaan Mission

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, JavaScript, Three.js
- **Templating**: Jinja2
- **Deployment**: Uvicorn

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/govindrnaik/3d-universe.git
   cd 3d-universe
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install fastapi uvicorn jinja2
   ```

## Usage

Run the application using:

```
python app.py
```

Or with Uvicorn directly:

```
uvicorn app:app --reload
```

The application will be available at http://127.0.0.1:8000/

## Project Structure

```
3d-universe/
├── app.py                 # Main FastAPI application
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # Project documentation
├── static/                # Static files (CSS, JS, images)
└── templates/             # Jinja2 HTML templates
    ├── base.html          # Base template with common elements
    ├── solar_system.html  # Solar system visualization
    ├── big_bang.html      # Big bang visualization
    ├── black_hole.html    # Black hole visualization
    └── ...                # Other visualization templates
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.