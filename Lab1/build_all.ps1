$sources = Get-ChildItem -Include *.cpp, *.c -Recurse | Resolve-Path -Relative
$srcCount = $sources.Count
$current = 1
foreach ($item in $sources) {
	$args = New-Object Collections.Generic.List[string]
	$args.Add($item.toString())
	$args.Add("-o")
	$args.Add($item.replace(".cpp", ".exe"))
	
    Write-Host "$current/$srcCount build $item"
	$current++
	& g++ $args
}