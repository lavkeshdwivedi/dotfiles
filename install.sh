#!/usr/bin/env bash
# Installs Claude Code skills to ~/.claude/commands/
set -e
COMMANDS_DIR="$HOME/.claude/commands"
mkdir -p "$COMMANDS_DIR"
cp -v claude/commands/*.md "$COMMANDS_DIR/"
echo "Skills installed to $COMMANDS_DIR"
