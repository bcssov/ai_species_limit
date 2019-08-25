py -3 publish.py
cd publish
cd ai_species_limit
Bandizip c -r "ai_species_limit.zip" "*.*"
xcopy "ai_species_limit.zip" "%UserProfile%\Documents\Paradox Interactive\Stellaris\mod" /y
cd .. 
cd ..
cls