$ErrorActionPreference = "Stop"
$buildDirName = "build"
$buildPath = ".\" + $buildDirName + "\"

if (!(Test-Path $buildPath)) {
    $pth = New-Item -Path ".\" -Name $buildDirName -ItemType "directory"
}

Write-Host "Cleanup"

Remove-Item -Path ($buildPath + "*") -Recurse

Write-Host "Prepare"

$sources = Get-ChildItem -Include *.cpp, *.c -Recurse | Resolve-Path -Relative
$exeName = "main.exe"
$buildArgs = New-Object Collections.Generic.List[string]
foreach ($item in $sources) {
    $buildArgs.Add($item.ToString())
}
$buildArgs.Add("-o")
$buildArgs.Add($buildPath + $exeName)
$buildArgs.Add("-Wall")
#$buildArgs.Add("-g")

Write-Host "Build"

& g++ $buildArgs

if ($LastExitCode -ne 0) {
    throw ("Build failed!")
}

Write-Host "Starting..."

&($buildPath + $exeName)

Write-Host ""