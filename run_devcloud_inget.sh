echo Iniciando job
source $HOME/miniconda3/bin/activate
conda activate llm
cd ~/Luis/rag
python main.py ingest
echo finalizou job

