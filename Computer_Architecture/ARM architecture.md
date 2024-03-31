main resource: https://www.amazon.com/Digital-Design-Computer-Architecture-ARM/dp/0128000562 

## Chapter 1 

![[Pasted image 20240331185643.png]]

[[Analog circuits]] - Used to make amplifiers; can input and output a continuous range of voltages

[[Digital  circuits]] - restrict voltages to discrete ranges, which we will use to indicate 0 and 1. 

[[Microarchitecture]] - links the logic and architecture levels of abstraction. 

[[architecture]] - abstraction describe a computer from the programmaer's perspective. 

### The digital abstraction

The amoutn of information D in a discrete valued variable with N distinct states is measured in units of bits as 
$$D = log_2 N$$bits

Bit is short for binary digit. 

Continuuous singla theoretical contain infinite amount of infomraiton. Inm pracitce, measurement error limit the information to only 10 to 16 bits for mosot cononitnuoos singals. 

George Boole developed system of logic operating on systems known as boolean logic. 

### Bytes, nibbles, and all that jazz
A group of eight bits is called a byte. It represents one of 2 8 = 256 possibilities. The size of objects stored in computer memories is customarily measured in bytes rather than bits.

A group of four bits, or half a byte, is called a nibble. It represents one of 2 4 = 16 possibilities. One hexadecimal digit stores one nibble and two hexadecimal digits store one full byte. Nibbles are no longer a commonly used unit, but the term is cute.

Microprocessors handle data in chunks called words. The size of a word depends on the architecture of the microprocessor. When this chapter was written in 2015, most computers had 64-bit processors, indicating that they operate on 64-bit words. At the time, older computers handling 32-bit words were also widely available. Simpler microprocessors, especially those used in gadgets such as toasters, use 8- or 16-bit words.

Microprocessor is a processor built on a single chip. 


### Logic gates
[[Buffer]] - From the logical point of view, a buffer is no different from a wire, so it might seem useless. However, from the analog point of view, the buffer might have desirable characteristics such as the ability to deliver large amounts of current to a motor or the ability to quickly send its output to many gates. This is an example of why we need to consider multiple levels of abstraction to fully understand a system; the digital abstraction hides the real purpose of a buffer.

### Beneath the digital abstraction

$V_{OL}$ => output low
$V_{IL}$ => input low
$V_{OH}$ => output high
$V_{IH}$ => input high

**[[Supply voltage]]**

**[[Logic Levels]]**

**[[Noise margins]]**
![[Pasted image 20240331191553.png]]


$V_{DD}$ stands for the voltage on the drain of a metal-oxidesemiconductor transistor, used to build most modern chips. The power supply voltage is also sometimes called $V_{CC}$ , standing for the voltage on the collector of a bipolar junction transistor used to build chips in an older technology. Ground is sometimes called $V_{SS}$ because it is the voltage on the source of a metal-oxidesemiconductor transistor.

**DC Transfer Characteristics**

DC indicates behavior when an input voltage is held constant or changes slowly enough for the rest of the system to keep up. The term’s historical root comes from direct current, a method of transmitting power across a line with a constant voltage. In contrast, the transient response of a circuit is the behavior when an input voltage changes rapidly.





