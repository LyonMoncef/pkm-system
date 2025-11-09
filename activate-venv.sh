#!/bin/bash
# activate-venv.sh
# Helper script pour activer l'environnement virtuel Python

PROJECT_ROOT="/mnt/c/Users/idsmf/Projects/pkm-system"
VENV_PATH="$PROJECT_ROOT/venv"

# Vérifier si venv existe
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ venv not found at $VENV_PATH"
    echo ""
    echo "Creating venv..."
    cd "$PROJECT_ROOT"
    python3 -m venv venv
    
    echo "Installing dependencies..."
    source venv/bin/activate
    pip install -r scripts/chat-atomizer/requirements.txt
    
    echo "✅ venv created and dependencies installed!"
else
    echo "✅ Activating venv..."
    source "$VENV_PATH/bin/activate"
fi

echo ""
echo "🐍 Python virtual environment active!"
echo "   Python: $(which python)"
echo "   Pip: $(which pip)"
echo ""
echo "💡 To deactivate: type 'deactivate'"
