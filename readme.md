### Description ###

I often use Magic Jack to talk to my parents.  However, one problem is that they can always call me, while I can only call them if the device is plugged in.

I decided that this was not acceptable, so I wrote Tango (The name comes from Django and Twilio - the technologies I'm using) in order to solve this.  Tango is hosted on Heroku.  When I call a certain number, Tango will email my parents telling them I'd like to talk with them.  It will then send me a confirmation SMS.

Why do that instead of just email them myself?  I'm often away from home without a computer, and I only have a limited data plan on my phone.  I figured this would be a cool alternative for myself, and anyone without access to the internet.

Tango was written in a couple of hours, and has much room for improvment.  Please feel free to report bugs and give me suggestions at vadrevu@berkeley.edu