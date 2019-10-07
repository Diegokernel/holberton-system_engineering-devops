
***

# My First Postmortem

### Issue Summary

Company wide system outage - Start: 3:08am PST - 4:11pm PST (13 hours)

Due to a power surge, the company server went down and caused physical damage to the hardware. Everything was down since all systems were linked to the server for login. All users working at current location were affected. The root cause was due to poor server maintenance.

### Timeline
* 3:08am PST - Company security alarm provider(ADT, BayAlarm, Ackerman...etc) alerted authorized personnel that their security monitoring systems were down. 
* 3:27am PST - Authorized personnel arrived on site and noticed all power in the building was off.
* 6:13am PST - Power was restored, but the server was still offline.
* 7:24am PST - First internal IT staff arrives and makes their best attempts to figuring out the issue.
* 9:00am PST - After finding out the server could not be powered on, the work for server repair/replacement was outsourced to an IT company after removing the hard drives to see what was salvageable.  
* 9:19am PST - Found backup drives with data that was at least 4 months behind due to improper configurations of the auto-backup scripts grabbing data from wrong location. Most likely caused by the system wide upgrade implemented around same time frame.  
* 10:47am PST - Found 3 of 10 hard drives from server failed. Started recovery of RAID10 setup and configuring a temporary server.
* 1:15pm PST - Temporary server is up and most company users are able to login.  
* 1:21pm PST - During the hard drive recovery, a power breaker reset due to too much power draw causing all data from the hard drives to corrupt.
* 4:11pm PST - Verified all data from server hard drives were unrecoverable and working with last known working configuration dated roughly 4 months back.   

### Root Cause
After a thorough investigation based on the events leading up to the server going down, the root cause of the server going down was caused by a faulty Uninterruptible Power Supply(UPS). Based on the model and internal IT knowledge, the UPS was over 10 years old and the battery has never been replaced. It was also noted that there have been at least 2 other power surges that have occured since, but no maintenance or physical checks of server equipment have been performed prior to this event. The most likely cause based on this evidence, is that the UPS had taken damage and could not provide its usual power surge protection after the second power surge leading to physical damage to the server hardware during this event.

### Corrective and Preventative Measures

To prevent future occurrences of this matter, the following preventative measures should be considered:

* Have at least 3 or more sources of data backup
    * Have at least 1 cloud based backup
    * Check those backups once a month or quarterly to verify integrity and proper functionality
* Clean the server physically!
    * Just like normal desktop (or even your car, home, self...etc) needs cleaning, so do servers.
* UPS maintenance
    * Replace the battery once every 3 years (at minimum) or sooner depending on battery life integrity
    * Replace immediately if your system recovers from a power surge/outage
* Have at least 2 servers
    * To prevent long downtimes and slower speeds
* Have a working monitoring system for your server
    * You should be able to receive alerts remotely from anywhere should anything go wrong with the server
