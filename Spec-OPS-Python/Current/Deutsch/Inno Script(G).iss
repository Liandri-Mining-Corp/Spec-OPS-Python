; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Optimizer
AppVersion=1.5
WizardStyle=modern
DefaultDirName={autopf}\Optimizer
DefaultGroupName=Optimizer
UninstallDisplayIcon={app}\Optimizer.exe
Compression=lzma2
SolidCompression=yes
; OutputDir=userdocs:Inno Setup Examples Output


[Files]
Source: "App (Deutsch).exe"; DestDir: "{app}"
Source: "Powerscheme.pow"; DestDir: "{app}"
Source: "boost(G).bat"; DestDir: "{app}"
Source: "deltemp(G).bat"; DestDir: "{app}"
Source: "Windows Privacy script.reg"; DestDir: "{app}"

[Icons]
Name: "{group}\Optimizer"; Filename: "{app}\App (Deutsch).EXE"; WorkingDir: "{app}"
Name: "{group}\Uninstall Optimizer"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Optimizer"; Filename: "{app}\App (Deutsch).EXE"; WorkingDir: "{app}"