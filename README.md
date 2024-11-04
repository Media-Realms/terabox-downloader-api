# Terabox Downloader API

A Flask-based API that allows users to download files from Terabox, a popular file hosting service.

## Features

- Download files from Terabox using an external API provider
- Retrieve file title, thumbnail, and available download resolutions
- Comprehensive error handling with appropriate HTTP status codes
- Detailed API documentation available at the `/docs` endpoint

## Getting Started

### Prerequisites

- Python 3.x
- pip package manager

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Media-Realms/terabox-downloader-api.git
   ```
2. Change to the project directory:
   ```
   cd terabox-downloader-api
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the API:
   ```
   python3 -m api
   ```
5. The API will be available at `http://localhost:5000/`.

### Deployment

The API can be deployed to various cloud platforms, such as Vercel, Heroku, or AWS.

To deploy to Vercel, you can use the provided `vercel.json` configuration file. Make sure you have the Vercel CLI installed and authenticated, then run the following commands:

```
vercel
vercel --prod
```

## Watch Youtube video for how to deploy github repo on vercel 

[YTVIDEO](https://youtu.be/uJq7hpULx0g?si=uFD83t5OQ5dUa1U2)

## API Documentation

Detailed API documentation is available at the `/docs` endpoint.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).