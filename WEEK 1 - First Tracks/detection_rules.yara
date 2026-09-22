/*
  OffSec Arctic Howl Season 2 - Week 1 Detection Rules
  YARA rules for macOS Xcode Supply Chain Compromise & AppleScript Payloads
*/

rule ArcticHowl_W1_Xcode_Dropper {
    meta:
        description = "Detects triple-hex encoded xcassets.sh dropper"
        author = "Rudra Sharma"
        reference = "OffSec Arctic Howl Week 1"
        severity = "High"
    strings:
        $s1 = "xxd -r -p" ascii nocase
        $s2 = "bu1knames.io" ascii
        $hex_pattern = /[0-9a-fA-F]{64,}/
    condition:
        all of ($s*) or ($hex_pattern and $s2)
}

rule ArcticHowl_W1_AppleScript_C2 {
    meta:
        description = "Detects nested Base64 AppleScript execution used by looz/jez"
        author = "Rudra Sharma"
        reference = "OffSec Arctic Howl Week 1"
        severity = "Critical"
    strings:
        $osascript = "osascript -e" ascii
        $b64_pipe = "base64 -d" ascii
        $serial_harvest = "ioreg -l" ascii nocase
    condition:
        $osascript and $b64_pipe and $serial_harvest
}
