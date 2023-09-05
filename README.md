# STP tutorial problems 

I'll try to get chatGPT to write most code

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