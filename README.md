# Recommendation System

## Overview
This project is a simple recommendation system consisting of two services: `Generator` and `Invoker`. The `Generator` service produces random recommendations, while the `Invoker` service manages the caching and coordinates multiple calls to the `Generator` service.

### Project Structure
- **Generator**: Generates random recommendations based on the provided model name.
- **Invoker**: Invokes the `Generator` service, caches the results locally and in Redis, and returns the combined recommendations.

## Installation and Setup

### Prerequisites
- Docker and Docker Compose installed on your system.
- Redis server if you are testing outside of Docker.

### Clone the Repository
```bash
git clone <repository_url>
cd recommendation-system
