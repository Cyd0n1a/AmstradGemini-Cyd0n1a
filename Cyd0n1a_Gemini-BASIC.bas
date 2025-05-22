10 REM ---(c) 2025 Cydonis Heavy Industries Ltd. Amstrad CPC BASIC Gemini API Client (Prototype v0.1a) ---
20 REM Assumes a serial interface proxy server (Raspi4B+) and AMSDOS-compatible driver
30 REM are present and configured (e.g., for stream #8, device "S")
40 REM --------------------------------------------------------
50 MODE 1 : REM 40-column text mode for clarity
60 BORDER 0 : PAPER 0 : INK 1 : CLS
70 PRINT CHR$(23);CHR$(1) : REM Disable firmware messages for cleaner serial
80 PRINT TAB(5);"--- CPC Gemini API Client ---"
90 PRINT
100 PRINT "Initialising Serial Port..."
110 LET serialDevice$="S" : REM Or "SCRS:", check your interface docs
120 LET streamNum=8
130 LET endMarker$="ENDOFRSP" : REM Pi should send this or an empty line

140 REM --- Main Program Loop ---
150 ON ERROR GOTO 500 : REM Jump to enhanced error handler

160 PRINT : PRINT "Enter your prompt for Gemini (or type QUIT):"
170 LINE INPUT prompt$
180 IF UPPER$(prompt$)="QUIT" THEN GOTO 950 : REM Jump to clean exit

190 IF prompt$="" THEN PRINT "Prompt cannot be empty." : GOTO 160

200 REM --- Send Prompt to Serial ---
210 PRINT "Sending prompt..."
220 OPENOUT "#"+STR$(streamNum)+","+serialDevice$
230 PRINT #streamNum, prompt$
240 CLOSEOUT #streamNum
250 PRINT "Prompt sent. Waiting for response..."
260 PRINT "(This may take a while...)"

270 REM --- Receive Response from Serial ---
280 LET responseComplete = 0
290 OPENIN "#"+STR$(streamNum)+","+serialDevice$
300 PRINT : PRINT "--- Gemini's Response ---"

310 WHILE NOT responseComplete
320   LINE INPUT #streamNum, line$
330   REM Check for end marker or empty line from Pi
340   IF line$="" OR UPPER$(line$)=endMarker$ THEN
350     responseComplete = 1
360   ELSE
370     PRINT line$
380   ENDIF
390 WEND
400 CLOSEIN #streamNum
410 PRINT "-------------------------"
420 PRINT
430 GOTO 150 : REM Loop for another prompt

440 REM TODO Lines 440-490 are now part of the error handler or exit routine.

450 REM --- Enhanced Error Handler ---
460 REM Note to self: Original lines 450-470 (old END sequence) are removed/replaced.
470 REM Original error handler started at 500, now effectively starts here.

500 ON ERROR GOTO 0 : REM Disable error trapping within handler itself
510 PRINT CHR$(7) : REM Beep to alert user
520 PRINT CHR$(23);CHR$(0) : REM Re-enable firmware messages (if disabled)
530 PRINT : PRINT "*** PROGRAM ERROR ***"
540 PRINT "ERROR CODE: ";ERR
550 PRINT "IN LINE   : ";ERL
560 PRINT "---------------------"

570 REM --- Specific Error Messages ---
580 IF ERR=5 THEN PRINT "Invalid argument in BASIC command."
590 IF ERR=12 THEN PRINT "Serial Device not found or not ready."
600 IF ERR=13 THEN PRINT "Serial Device already open."
610 IF ERR=14 THEN PRINT "Serial Channel not free/invalid."
620 IF ERR=17 THEN PRINT "Device I/O Error. Check connection/settings."
630 IF ERR=20 THEN PRINT "End of file reached unexpectedly." : PRINT "(Connection lost or Pi script ended?)"
640 IF ERR=26 THEN PRINT "Syntax error (e.g., FOR without NEXT)."
650 IF ERR=27 THEN PRINT "Out of memory."
660 IF ERR=0 AND ERL<>0 THEN PRINT "Unknown error or error handler issue." : REM ERL<>0 to avoid message if ON ERROR GOTO 0 is hit directly

670 PRINT "---------------------"
680 PRINT "Attempting to close serial streams..."
690 CLOSEIN #streamNum : REM Attempt to close, will error if not open, handled by ON ERROR GOTO 0
700 CLOSEOUT #streamNum : REM Attempt to close
710 PRINT "Streams closed (if they were open)."
720 PRINT

730 REM --- User Choice for Recovery ---
740 PRINT "Choose an option:"
750 PRINT " (R)etry operation (if applicable)"
760 PRINT " (C)ontinue to next prompt"
770 PRINT " (Q)uit program"
780 PRINT
790 LET choice$=""
800 WHILE choice$=""
810   choice$=UPPER$(INKEY$)
820 WEND

830 IF choice$="R" THEN
840   PRINT "Retrying operation..."
850   ON ERROR GOTO 500 : REM Re-enable main error handler before resuming
860   RESUME : REM Retries the statement that caused the error
870 ELSEIF choice$="C" THEN
880   PRINT "Continuing to next prompt..."
890   ON ERROR GOTO 500 : REM Re-enable main error handler
900   RESUME 150 : REM Go back to the main loop start
910 ELSEIF choice$="Q" THEN
920   PRINT "Quitting..."
930   GOTO 950 : REM Jump to clean END sequence
940 ELSE
950   PRINT "Invalid choice. Quitting."
960   GOTO 950 : REM Jump to clean END sequence
970 ENDIF

940 REM --- Clean Program Exit ---
950 PRINT CHR$(23);CHR$(0) : REM Re-enable firmware messages
960 PRINT : PRINT "Closing streams and exiting..."
970 ON ERROR GOTO 0 : REM Prevent errors during final close attempt
980 CLOSEIN #streamNum
990 CLOSEOUT #streamNum
1000 PRINT "Exited Gemini Client."
1010 PRINT "// (c) 2025 Cydonis Heavy Industries, Ltd."
1020 END