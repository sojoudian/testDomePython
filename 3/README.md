You are receive a string that contains an XML log file like the following:

<?xml version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>

Implement a function ids_by_message that returns the ids of the entries that contain a specific message. The ids should be integer values and the array does not need to be sorted.

For example, ids_by_message for the XML log above and the message "Application ended" should return [2].
