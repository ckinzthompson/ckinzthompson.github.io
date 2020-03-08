---
layout: posts
author: Colin Kinz-Thompson
title: AOM Controller Project
date: 2016-07-20
---
# AOM Controller Documentation

I built a Controller unit to control ISOMET digital-input controlled Acousto-Optic Modulators (AOM). We bought one IMDD-P80L unit ([](http://www.isomet.com/AO_Pdf/IMDD-P80L-1.pdf)).

To control the unit, you must interface with the following plug — schematic:
![Plug Schematic](/images/aom/plugschematic.png)
----
The built-in RF driver requires a 12 V source to generate the acoustic waves in the crystal. This needs to be relatively stable to avoid fluctuations. Also, a digital (3-5 V on) signal must be applied to the MOD pin in order to trigger the acoustic wave, and create the modulation. The idea behind this controller unit is to regulate a voltage source higher than 12 V down to 12V, and then to apply the modulation signal using an Arduino digital out pin.

This controller is built to control up to four AOM units, with the last two having the same modulation signal (for simultaneous triggering). In total, that means there are three digital out pins used.

## Program the Modulation

To program the Arduino to produce the modulation signal, use the following code

{% highlight C %}
// Port registers PORTy, where y =
// B (digital pin 8 to 13)
// C (analog input pins)
// D (digital pins 0 to 7)

// send it a 8-bit binary (B) number to set the entire register
// e.g. const int pins = B00000010; // -,-,digital 13, digital 12, 11,10,9,8
//  and const int pins = B00000010; // digital 7,6,5,4,3,2,1,0

const int pins = B00000100;
const int off = B00000000;

void setup() {
  DDRD = pins;
  PORTD &= off;
 }
#define high (PORTD = pins);
#define low (PORTD = off);
{% endhighlight %}

This will set up digital pin 2 to be able to create a digital modulation signal. To actually generate the signal with the timings you need the loop function. For relative slow modulations (maybe < 100 kHz), you can probably get away with using the delay function. For instance

{% highlight C %}
void loop() {
   while(1){
     high;
     delay(500);
     low;
     delay(500);
   }
}
{% endhighlight %}

If you need fast signals, you have to consider the clock speed of the Arduino. The Arduino Duo runs at 16 Mhz clock speed — that means that you can execute one instruction every 62.5 sec. If you want to work this fast you should know about the ringing/rise-time of the signal, but more importantly, you must consider any program overhead, such as evaluating conditions in loops. A `while` loop takes two clock cycles every loop. Therefore, the minimum, repeated 50% duty cycle signal you can generate is three clock cycles on, and then three clock cycles off. To do this, try:

{% highlight C %}
void loop(){
   while(1){
     high;
     high;
     high;

     low; // There would otherwise be two more low entries here, but going to the start and check whether the loop is down takes up the space for those. Therefore, there's no need to stall.
   }
}
{% endhighlight %}

## Build the Electronics
Schematic Drawing:
![Schematic](/images/aom/schematic.png)
---
Outside View:
![Outside](/images/aom/outside.png)
---
Inside View:
![Inside](/images/aom/inside.png)
---
## Notes:
* The DC jack/wall-wart adapter I bought aren’t compatible for some reason… therefore, I chopped the DC plug off, and soldered it straight to the leads of the jack (threaded through a hole in the jack).
* The 12 V regulator runs pretty hot, therefore the fan should probably be positioned over this.
* The AOMs run very hot — make sure not to keep them on for too long.
* If the USB is plugged in, the 5V power from the USB line can power the rails a little. Therefore, the front LED will be on, and the fan will run, and probably the AOM will get hot, even though the the power switch on the front will be off! Just unplug the USB when you’re done.
* The top rows 15-30 on the bread-board are for the AOM plugs. For instance, the unit controlled by digital out 2 should be: (15) 12 V, (16) 0 V, (17) 0 V, (18) Modulation-D1. The one controlled by digital out 3 should be (19) 12 V, (20) 0 V, (21) 0 V, (22) Modulation-D2.
* The modulation signal produced by digital out 3 is sent to the modulation pin for two devices so that they might be controlled simultaneously. These should be wired to device 1: (23) 12 V, (24) 0V, (25) 0V, (26) Modulation-D3, and device 2: (27) 12 V, (28) 0V, (29) 0V, (30) Modulation-D3.
