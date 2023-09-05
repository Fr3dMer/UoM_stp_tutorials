# STP tutorial problems 


My goal here is to see how ChatGPT can be applied to these tutorial problems. I have created the main.py structure and the general class structures, witht he goal of ChatGPT filling in the rest. The chat bot began to strugle as the requirments got more complicated, especially problem ex2.3.


# Run the script
```bash
python3 main.py \
--ex1 ex1.1,ex1.2,ex1.3,ex1.4,ex1.5 \
--ex2 ex2.1,ex2.2,ex2.3,ex2.4,ex2.5,ex2.6
```


# Download and install dependencies in conda env
```bash
git clone --branch "main" "https://github.com/Fr3dMer/UoM_stp_tutorials.git" 
cd UoM_stp_tutorials
conda create --name UoM_stp_tutorials pip
conda activate UoM_stp_tutorials
pip install -r requirements.txt
```

# Save env
```bash
pipreqs --force . 
```

Plan 
- [x] Create logging module
- [x] Create arg parser
- [ ] Tests for Exercise 1 
- [x] Exercise 1
- [ ] Tests for Exercise 2 
- [ ] Exercise 2
- [ ] Tests for Exercise 3 
- [ ] Exercise 3
- [ ] Tests for Exercise 4 
- [ ] Exercise 4 