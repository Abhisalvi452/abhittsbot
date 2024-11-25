#!/bin/bash

# Exit on error
set -e

echo "Setting up Text-to-Speech Converter App development environment..."

# Update packages
echo "Updating package repositories..."
pkg update -y && pkg upgrade -y

# Install required packages
echo "Installing required packages..."
pkg install -y python git wget curl build-essential

# Create project directory
echo "Creating project directory..."
mkdir -p ~/tts-app
cd ~/tts-app

# Create virtual environment
echo "Setting up Python virtual environment..."
python -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install kivy edge-tts buildozer

# Create the main app file
echo "Creating app files..."
cat > main.py < /path/to/main.py/content

# Create buildozer spec file
cat > buildozer.spec < /path/to/buildozer.spec/content

echo "Setup complete!"
echo ""
echo "To build the APK:"
echo "1. Make sure you have enough storage space (at least 4GB free)"
echo "2. Run 'buildozer android debug'"
echo "3. The APK will be created in the 'bin' directory"
echo ""
echo "Note: Building in Termux might take significant time and resources."
echo "Consider building on a Linux computer for better performance."
