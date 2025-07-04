# Battery Monitoring Platform

This monorepo contains the code for an end-to-end IoT battery monitoring platform.

## Sub-projects

*   **backend**: FastAPI backend for handling battery logs and real-time updates.
*   **web-client**: React web client for visualizing battery data.
*   **android-rootapp**: Android application for monitoring battery status.

## Getting Started

### Backend

To run the backend, you need Docker and Docker Compose.

1.  Navigate to the `backend` directory.
2.  Run `docker-compose up --build`.

The backend will be available at `http://localhost:8000`.

### Web Client

To run the web client, you need Node.js and npm.

1.  Navigate to the `web-client` directory.
2.  Run `npm install`.
3.  Run `npm start`.

The web client will be available at `http://localhost:3000`.

### Android App

To run the Android app, you need Android Studio.

1.  Open the `android-rootapp` directory in Android Studio.
2.  Build and run the app on an emulator or a physical device.
