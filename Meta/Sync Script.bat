@echo off
echo Syncing brain- vault with GitHub...
cd /d "C:\Users\rajuc\Documents\brain-"
git add .
git commit -m "Daily sync - %date% %time%"
git push origin main
echo Sync complete!
pause
