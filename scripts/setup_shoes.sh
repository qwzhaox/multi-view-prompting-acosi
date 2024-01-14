task=$1

# Path to the script that needs to be modified
run_main="scripts/run_main.sh"
const="src/const.py"

create_delete_dirs() {
    task1=$1
    task2=$2

    if [ ! -d "../multi-view-prompting-acosi/data/$task1/shoes" ]; then
        if [ $task1 = "acosi" ]; then
            mkdir -p ../multi-view-prompting-acosi/data/$task1
        fi
        mkdir -p ../multi-view-prompting-acosi/data/$task1/shoes
    fi
    if [ -d "../multi-view-prompting-acosi/data/$task2/shoes" ]; then
        rm -rf ../multi-view-prompting-acosi/data/$task2/shoes
        if [ $task2 = "acosi" ]; then
            rm -rf ../multi-view-prompting-acosi/data/$task2
        fi
    fi
}

comment() {
    line=$1
    file=$2
    sed -i "$line {/^#/!s/^/#/}" "$file"
}

uncomment() {
    line=$1
    file=$2
    sed -i "$line s/^#//" "$file"
}

if [ "$task" = "acos" ]; then
    comment 7 "$run_main"
    uncomment 8 "$run_main"
    comment 11 "$run_main"

    uncomment 170 "$const"
    comment 171 "$const"

    comment 208 "$const"
    uncomment 209 "$const"
    comment 210 "$const"

    uncomment 229 "$const"
    comment 231 "$const"
    comment 232 "$const"
    comment 233 "$const"

    create_delete_dirs acos acosi
    cd ../Shoes-ACOSI
    bash scripts/bash/convert_json_txt_for_mvp.sh -acos
    bash scripts/bash/acosi_to_mvp.sh acos
elif [ "$task" = "acosi" ]; then
    uncomment 7 "$run_main"
    comment 8 "$run_main"
    uncomment 11 "$run_main"

    comment 170 "$const"
    uncomment 171 "$const"

    uncomment 208 "$const"
    comment 209 "$const"
    uncomment 210 "$const"
    
    comment 229 "$const"
    uncomment 231 "$const"
    uncomment 232 "$const"
    uncomment 233 "$const"

    create_delete_dirs acosi acos
    cd ../Shoes-ACOSI
    bash ../Shoes-ACOSI/scripts/bash/convert_json_txt_for_mvp.sh -acosi
    bash ../Shoes-ACOSI/scripts/bash/acosi_to_mvp.sh acosi 
else
    echo "task not found"
    exit 1
fi
