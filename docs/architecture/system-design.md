System Design

Current Architecture

Browser ↓ Swagger UI ↓ FastAPI ↓ Upload Endpoint ↓ Local Storage



MVP Architecture

Browser ↓ FastAPI ↓ Upload Endpoint ↓ SQLite ↓ Photo Catalog



Future Architecture

Browser ↓ React UI ↓ FastAPI ↓ SQLite Database ↓ Photo Metadata



&#x20;   +

TensorFlow Models



Tie Dye Classifier

Location Classifier

Animal Classifier

Person-Type Classifier

Data Flow

Upload Photo ↓ Save To Disk ↓ Store Database Record ↓ Run ML Models ↓ Store Predictions ↓ Display Results



Technology Stack

Frontend:



React

TypeScript

TailwindCSS

Backend:



FastAPI

Python

Machine Learning:



TensorFlow

Keras

Database:



SQLite

Deployment:



Docker

