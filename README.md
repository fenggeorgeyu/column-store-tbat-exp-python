# Experiment Code for Column-Store Write Optimization
LICENSE: GPL V2  
Author: Feng "George" Yu  
Initial Date: Jun, 2014  
Updated Date: Sep 22, 2016


This repo is the first version of the write optimization experiments on OOC (out-of-core) column-store databases. We implement [TBAT (Timestamped Binary Association Table)][^yu-dexa15] to compare with [BAT (Binary Association Table)][^bat]. 

## Folder Structure

### prepare
Basic classes used for creating, reading, and updating data.

### exp_update

Experiment code for write experiments (TBAT vs BAT).  
`config.py` stores experiment parameters.  
`exp_prepareData.py` initialize experiment datasets of TBAT and BAT.  
`exp_prepareUpdateLists.py` prepares update files to be written on TBAT and BAT.  
`exp_updateData*.py` are different versions of writing operations on TBAT and BAT to merge the update list (update files) into the original TBAT and BAT. The 3rd version includes removing outliers and calculating statistics.


### merge_update

After the AOC update, we will use `merge_update.py` to clean (or smartly merge) the updated date which is appended at the end of the TBAT to replace the original data records. This is actually referred as offline data cleaning after AOC update.

### script

`run_exp_update_slow_multiple_batch.sh` is an automatic script to run multiple experiments with different parameters. The experiment result will be automatically sent to you via email with the help of `sendEmail`. Please make sure you change the email settings at the bottom of the script. When running this script the only required input is your email password. If you are working on a long time experiment, please use the command `screen` to work in a non-interruptible SSH connection.

### data

Some previous experiment results are listed for your reference.

### test_1

My python test code folder.

[^yu-dexa15]: http://link.springer.com/chapter/10.1007%2F978-3-319-22849-5_12 
[^bat]: http://dl.acm.org/citation.cfm?id=1142527








 



