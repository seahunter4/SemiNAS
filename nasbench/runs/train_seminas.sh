cd ..
export PYTHONPATH=.:$PYTHONPATH
MODEL=seminas
OUTPUT_DIR=outputs/$MODEL

mkdir -p $OUTPUT_DIR

for i in {11..25}
do
  python train_seminas.py \
    --output_dir=$OUTPUT_DIR \
    | tee $OUTPUT_DIR/log0105_$i.txt
done
