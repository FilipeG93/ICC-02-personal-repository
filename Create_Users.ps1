Import-Module ActiveDirectory

$csvPath = "C:\lab18\newusers.csv"

$ouPath = "OU=NewUsers,DC=greenbloom,DC=ltd"

$users = Import-Csv -Path $csvPath

foreach ($user in $users) 
{
    
    $firstName = $user.FirstName
    $lastName = $user.LastName
    $username = $user.Username
    $password = $user.Password
    $department = $user.Department
    $displayName = "$firstName $lastName"

    Write-Host "Creating account for $displayName..."

    New-ADUser `
        -Name $displayName `
        -GivenName $firstName `
        -Surname $lastName `
        -SamAccountName $username `
        -UserPrincipalName "$username@greenbloom.ltd" `
        -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) `
        -Enabled $true `
        -ChangePasswordAtLogon $true `
        -Path $ouPath

        Add-ADGroupMember -Identity $department -Members $username
        Write-Host "$displayName was added to $department group"

}

Write-Host "Done! All users created and added to their groups."

