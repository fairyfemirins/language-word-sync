# Cleanup Required

The virtual environment (`venv/`) was accidentally committed to the repository. To clean it up, run the following commands:

```bash
cd ~/projects/language-word-sync
rm -rf venv/
echo "venv/" >> .gitignore
git add .gitignore
git commit -m "Remove virtual environment from repository"
```