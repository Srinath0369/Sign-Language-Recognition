# Sign Language Recognition Web Application

A real-time sign language recognition system that uses computer vision and machine learning to interpret sign language gestures through both live camera feed and video uploads.

## Features

- **Real-time Recognition**: Live camera feed for instant sign language detection
- **Video Upload**: Upload pre-recorded videos for sign language analysis
- **Modern UI**: Clean, responsive interface with real-time prediction display
- **Cross-platform**: Works on desktop and mobile browsers
- **Instant Results**: Real-time prediction output with confidence scores

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask
- **Machine Learning**: TensorFlow/Keras, MediaPipe Holistic
- **Computer Vision**: OpenCV, MediaPipe
- **Deployment**: Heroku-ready with Procfile

## Project Structure

```
model/
├── main.py                 # Flask application entry point
├── predictions.py          # ML prediction logic
├── models.py              # Data models and database schema
├── database.py            # Database configuration
├── BaseModels.py          # Base model classes
├── static/
│   ├── index.html         # Main application page
│   ├── features.html      # Features page
│   ├── about.html         # About page
│   ├── script.js          # Main JavaScript functionality
│   ├── style.css          # Application styling
│   └── styles.css         # Additional styles
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment configuration
├── runtime.txt           # Python runtime version
└── holistic-custom-*.h5  # Trained ML model
```

## Installation and Setup

### Prerequisites

- Python 3.9+
- Node.js (for development tools, optional)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sign-language-recognition.git
   cd sign-language-recognition
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000`

### Deployment

This application is configured for Heroku deployment:

1. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

2. **Deploy**
   ```bash
   git push heroku main
   ```

## Usage

### Live Camera Mode
1. Click "Start Camera" to enable webcam
2. Position yourself in front of the camera
3. Perform sign language gestures
4. View real-time predictions in the output panel

### Video Upload Mode
1. Click "Upload Video" to select a video file
2. Choose a video file containing sign language
3. Click "Process Video" to analyze
4. View prediction results
5. Use "Cancel Upload" to reset if needed

## Features Implemented

- ✅ Real-time camera-based sign language detection
- ✅ Video upload and processing capabilities
- ✅ Modern, responsive UI design
- ✅ Prediction confidence display
- ✅ Upload cancellation functionality
- ✅ Seamless mode switching
- ✅ Error handling and validation
- ✅ Mobile-friendly interface

## Recent Updates

- Removed unnecessary UI elements for cleaner interface
- Added cancel upload functionality
- Enhanced prediction output display
- Fixed upload workflow bugs
- Improved error handling
- Added responsive design elements
- Optimized JavaScript performance

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Process live camera frames
- `POST /upload` - Handle video file uploads
- `GET /features` - Features information page

## Browser Compatibility

- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 80+

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe team for the holistic pose detection
- TensorFlow team for the machine learning framework
- OpenCV community for computer vision tools

## Support

For questions or issues, please open an issue on GitHub or contact the development team.
