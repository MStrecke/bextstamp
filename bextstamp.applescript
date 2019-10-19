#!/usr/bin/osascript

on run
	return "done"
end run

on process_item(this_item)
	set mypro to POSIX path of (path to resource "bextstamp.py")
	set this_item_quoted to quoted form of this_item

	try
		do shell script ("python " & mypro & " " & this_item_quoted)
	on error errmsg number errnr
		set errorMessage to "Error " & errnr & " during processing of " & this_item
		display dialog errorMessage buttons {"Sh!t"}
	end try
end process_item

on open these_items
	repeat with i from 1 to the count of these_items
		set this_item to item i of these_items
		set this_file to quoted form of POSIX path of this_item
		process_item(this_file)
	end repeat
	display notification "Processing complete"
end open
