# 🎙️ MVP Audio Transcription Service

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.8-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-performance, real-time audio transcription service built with FastAPI and OpenAI's Whisper model. Convert your audio files to text instantly and download professional PDF transcripts.

## 🚀 Features

- ⚡ **Real-time Processing**: Instant transcription without background queues
- 🎯 **High Accuracy**: Powered by OpenAI's Whisper base model
- 📄 **PDF Export**: Professional PDF generation with proper formatting
- 🔧 **GPU Acceleration**: Automatic CUDA detection for faster processing
- 📁 **Multi-format Support**: MP3, M4A audio file support
- 🌐 **RESTful API**: Clean, documented API endpoints

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **AI Model**: OpenAI Whisper (via Hugging Face Transformers)
- **PDF Generation**: ReportLab
- **Deep Learning**: PyTorch with CUDA support
- **File Processing**: Python multipart handling

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Optional: CUDA-capable GPU for faster processing

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gifted-Dev/mvp_audio_transcription.git
   cd mvp_audio_transcription
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Start

1. **Start the development server**
   ```bash
   uvicorn fastapi.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Alternative Documentation: http://localhost:8000/redoc

## 📚 API Usage

### Upload Audio File

**Endpoint**: `POST /upload_files`

```bash
curl -X POST "http://localhost:8000/upload_files" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_audio_file.mp3"
```

**Response**:
```json
{
  "message": "Transcription completed!",
  "transcription": "Your transcribed text will appear here...",
  "pdf_download_link": "/download/12345678-1234-5678-9012-123456789abc"
}
```

### Download PDF Transcript

**Endpoint**: `GET /download/{file_id}`

```bash
curl -X GET "http://localhost:8000/download/12345678-1234-5678-9012-123456789abc" \
     --output transcript.pdf
```

## 🔧 Configuration

### Supported Audio Formats
- MP3 (.mp3)
- M4A (.m4a)

### Environment Variables

Create a `.env` file in the root directory for custom configurations:

```env
# Server Configuration
HOST=0.0.0.0
PORT=8000

# Model Configuration
WHISPER_MODEL=openai/whisper-base
DEVICE=auto  # auto, cuda, cpu

# File Storage
UPLOAD_DIR=uploads
MAX_FILE_SIZE=50MB
```

## 📁 Project Structure

```
mvp_audio_transcription/
├── fastapi/
│   ├── __pycache__/
│   └── main.py              # Main FastAPI application
├── uploads/                 # Audio files and generated PDFs
├── .venv/                  # Virtual environment
├── .git/                   # Git repository
├── .gitignore             # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🧪 Testing

### Manual Testing

1. Start the server
2. Visit http://localhost:8000/docs
3. Use the interactive API documentation to test endpoints

### Example Test Files

Test with sample audio files:
- Short recordings (< 30 seconds) for quick testing
- Various formats (MP3, M4A)
- Different audio qualities

## 🚀 Deployment

### Docker Deployment (Recommended)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Deployment

```bash
# Using Gunicorn for production
pip install gunicorn
gunicorn fastapi.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 🔍 Performance Optimization

- **GPU Acceleration**: Automatically uses CUDA if available
- **Model Caching**: Whisper model loaded once at startup
- **File Management**: Temporary files cleaned up after processing
- **Memory Efficiency**: Streaming file uploads for large files

## 🛡️ Security Considerations

- File type validation
- File size limits
- Input sanitization
- Temporary file cleanup

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the excellent speech recognition model
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [Hugging Face](https://huggingface.co/) for model hosting and transformers library

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Gifted-Dev/mvp_audio_transcription/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

## 🗺️ Roadmap

- [ ] Web frontend interface
- [ ] Batch processing support
- [ ] Multiple language detection
- [ ] User authentication
- [ ] Cloud storage integration
- [ ] WebSocket real-time streaming
- [ ] Advanced PDF formatting options

---

**Made with ❤️ by [Gifted-Dev](https://github.com/Gifted-Dev)**
