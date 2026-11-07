#Requires -Version 5.1
#Requires -RunAsAdministrator
<#
.SYNOPSIS
EIT: audits or removes only the consumer Microsoft.Copilot package.
.DESCRIPTION
Defaults to audit. Pass -Remediate to request removal; -WhatIf remains supported.
Does not remove Microsoft 365 Copilot/Office Hub or any other application.
Review local-data impact and pilot results before assigning remediation.
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
param([switch]$Remediate)

$ErrorActionPreference = 'Stop'
$consumerPackageName = 'Microsoft.Copilot'
$installedPackages = @(Get-AppxPackage -AllUsers -Name $consumerPackageName -PackageTypeFilter Main)
$provisionedPackages = @(Get-AppxProvisionedPackage -Online | Where-Object { $_.DisplayName -eq $consumerPackageName })
$removalResults = @()

foreach ($package in $installedPackages) {
    if ($package.Name -ne $consumerPackageName) { throw 'Unexpected installed package identity.' }
    $action = 'AuditOnly'
    if ($Remediate -and $PSCmdlet.ShouldProcess($package.PackageFullName, 'Remove consumer Copilot for all users')) {
        Remove-AppxPackage -Package $package.PackageFullName -AllUsers -ErrorAction Stop
        $action = 'Removed'
    }
    $removalResults += [pscustomobject]@{ Type = 'Installed'; Package = $package.PackageFullName; Action = $action }
}

foreach ($package in $provisionedPackages) {
    if ($package.DisplayName -ne $consumerPackageName) { throw 'Unexpected provisioned package identity.' }
    $action = 'AuditOnly'
    if ($Remediate -and $PSCmdlet.ShouldProcess($package.PackageName, 'Remove consumer Copilot provisioning for new profiles')) {
        Remove-AppxProvisionedPackage -Online -PackageName $package.PackageName -ErrorAction Stop | Out-Null
        $action = 'Removed'
    }
    $removalResults += [pscustomobject]@{ Type = 'Provisioned'; Package = $package.PackageName; Action = $action }
}

[pscustomobject]@{
    PackageName = $consumerPackageName
    RemediationRequested = [bool]$Remediate
    FoundCount = $installedPackages.Count + $provisionedPackages.Count
    Results = $removalResults
} | ConvertTo-Json -Depth 4
