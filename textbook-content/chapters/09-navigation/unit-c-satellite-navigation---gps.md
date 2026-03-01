---
wingwing_chapter: 9
wingwing_unit: "C"
unit_title: "Satellite Navigation - GPS"
faa_sources: ['PHAK - Chapter 16 - Navigation.pdf']
estimated_read_time: 42
---

# Unit C: Satellite Navigation - GPS

Imagine having a constellation of 24 satellites orbiting 12,000 miles above Earth, each one precisely timing signals to help you navigate anywhere on the planet within just a few meters. The Global Positioning System (GPS) has revolutionized aviation navigation, transforming how pilots plan routes, execute approaches, and maintain situational awareness. Understanding GPS technology and its proper application is essential for modern pilots who rely on this remarkable system for safe and efficient flight operations.

## Learning Objectives

After completing this unit, you will be able to:

- Explain the fundamental principles of GPS operation and describe the basic components of the satellite navigation system
- Identify sources of GPS error and evaluate factors that affect navigation accuracy in flight operations
- Understand Receiver Autonomous Integrity Monitoring (RAIM) concepts and determine when GPS navigation is reliable
- Describe Wide Area Augmentation System (WAAS) capabilities and recognize its benefits for precision approaches
- Apply proper GPS navigation procedures and demonstrate correct operational techniques during flight
- Recognize GPS system limitations and comply with applicable regulatory requirements for GPS-equipped aircraft
- Plan GPS flights effectively and perform thorough preflight procedures for satellite navigation equipment
- Troubleshoot common GPS malfunctions and execute appropriate emergency procedures when GPS navigation fails

---

## GPS FUNDAMENTALS AND SYSTEM OVERVIEW

The **Global Positioning System (GPS)** has revolutionized aviation navigation since its introduction to civilian aviation in the 1980s. This satellite-based navigation system provides precise position, velocity, and time information to users worldwide, 24 hours a day, in all weather conditions. GPS represents a significant advancement over traditional ground-based navigation aids, offering pilots unprecedented accuracy and reliability for both VFR and IFR operations.

GPS navigation relies on a constellation of satellites orbiting Earth at approximately 12,550 nautical miles altitude. The system operates on the principle of **trilateration**, using precise time measurements from multiple satellites to determine an aircraft's exact position. Unlike VOR stations that provide bearing information relative to a fixed ground location, GPS provides absolute position information anywhere on Earth.

For pilots, GPS offers numerous advantages over conventional navigation systems. The system provides continuous position updates, eliminates the line-of-sight limitations of VHF navigation aids, and offers global coverage. Modern GPS receivers can store thousands of waypoints, display moving maps, and integrate with other aircraft systems to provide comprehensive navigation solutions.

### GPS Constellation and Satellite Configuration

The GPS constellation consists of a minimum of **24 operational satellites** arranged in six orbital planes, with each plane containing four satellites. This configuration ensures that at least four satellites are visible from any point on Earth at any time, which is the minimum number required for three-dimensional position determination.

The satellites orbit Earth every 12 hours at an altitude of approximately 12,550 nautical miles (20,200 kilometers). This **Medium Earth Orbit (MEO)** provides optimal coverage while maintaining reasonable signal strength at the Earth's surface. The orbital planes are inclined 55 degrees to the equator and are spaced 60 degrees apart, ensuring global coverage.

Each satellite weighs approximately 4,000 pounds and measures about 17 feet across with solar panels deployed. The satellites are powered by solar arrays and contain highly accurate atomic clocks that are essential for the precise time measurements required for GPS positioning. These **cesium and rubidium atomic clocks** maintain accuracy to within a few nanoseconds.

> **Satellite Health Monitoring**: The GPS constellation includes several spare satellites in orbit to ensure continuous service. When satellites require maintenance or fail, replacement satellites can be activated to maintain the minimum 24-satellite constellation.

The constellation is managed by the United States Space Force from the Master Control Station at Schriever Air Force Base in Colorado. Ground-based monitor stations worldwide track satellite orbits and clock performance, uploading corrections and navigation data to maintain system accuracy. This network ensures each satellite knows its precise orbital position and can broadcast accurate ephemeris data to GPS receivers.

Satellites broadcast their location using **ephemeris data**, which describes each satellite's orbital parameters. This information allows GPS receivers to calculate the precise position of each satellite at any given time. The ephemeris data is updated regularly and is valid for approximately four hours, though satellites continue broadcasting the same data set for up to six hours.

### Signal Structure and Transmission Principles

GPS satellites transmit navigation signals on two primary frequencies in the L-band spectrum. The **L1 frequency** operates at 1575.42 MHz, while the **L2 frequency** transmits at 1227.60 MHz. These frequencies were specifically chosen to minimize atmospheric interference and provide reliable signal propagation to ground-based receivers.

The L1 frequency carries the **Coarse/Acquisition (C/A) code**, which is available for civilian use and forms the basis of standard GPS navigation. This code repeats every millisecond and provides the fundamental ranging information used by civilian GPS receivers. The C/A code allows receivers to measure the time required for signals to travel from satellites to the receiver, enabling distance calculations.

Each satellite transmits a unique **Precision (P) code** on both L1 and L2 frequencies. The P code is reserved for military use and authorized civilian applications requiring higher accuracy. When encrypted, the P code becomes the **Y code**, which provides anti-spoofing protection for military users. Civilian aviation typically relies on the C/A code for standard navigation applications.

> **Signal Structure**: GPS signals use Code Division Multiple Access (CDMA) technology, allowing all satellites to transmit on the same frequencies simultaneously. Each satellite's unique code enables receivers to distinguish between different satellite signals.

The navigation message transmitted by each satellite contains essential information including satellite health status, clock correction parameters, and orbital data. This **50-bit-per-second data stream** provides the almanac and ephemeris information necessary for position calculations. The complete navigation message takes 12.5 minutes to transmit and is continuously repeated.

GPS signals are relatively weak when they reach Earth's surface, with power levels similar to a 25-watt light bulb viewed from 12,550 miles away. This low signal strength makes GPS susceptible to interference from electronic devices, atmospheric conditions, and physical obstructions. Modern aviation GPS receivers use sophisticated signal processing techniques to extract navigation information from these weak signals.

The **spread spectrum** nature of GPS signals provides inherent resistance to interference and allows multiple satellites to share the same frequency bands. Each satellite's pseudo-random code spreads the navigation signal across approximately 2 MHz of bandwidth, much wider than necessary for the 50-bit-per-second data rate. This spreading technique improves signal reliability and reduces susceptibility to narrow-band interference.

### Basic Positioning Theory and Trilateration

GPS positioning relies on the mathematical principle of **trilateration**, which determines position by measuring distances to known reference points. In GPS navigation, these reference points are satellites with precisely known orbital positions. By measuring the distance to multiple satellites simultaneously, a GPS receiver can calculate its exact position in three-dimensional space.

The fundamental concept involves measuring the time required for radio signals to travel from satellites to the receiver. Since GPS signals travel at the speed of light (approximately 186,000 miles per second), precise time measurements enable accurate distance calculations. A timing error of just one microsecond translates to a distance error of approximately 1,000 feet.

To determine a two-dimensional position (latitude and longitude), a GPS receiver must receive signals from at least **three satellites**. Each satellite measurement provides a circle of possible positions centered on that satellite. The intersection of three such circles yields two possible positions, only one of which is typically on or near the Earth's surface.

For three-dimensional positioning including altitude, a minimum of **four satellite signals** is required. The fourth satellite measurement eliminates the ambiguity present in two-dimensional fixes and provides altitude information essential for aviation applications. Most GPS receivers track signals from six to twelve satellites simultaneously to improve accuracy and provide redundancy.

> **Geometric Dilution of Precision**: The accuracy of GPS positioning depends partly on satellite geometry. When satellites are clustered together in the sky, small measurement errors translate to large position errors. Optimal accuracy occurs when satellites are widely distributed across the sky.

The trilateration process begins when the GPS receiver measures **pseudoranges** to visible satellites. These measurements are called pseudoranges rather than true ranges because they include clock errors in both the satellite and receiver. Satellite clocks are extremely accurate but not perfect, while receiver clocks are typically much less precise crystal oscillators.

GPS receivers solve for four unknowns: latitude, longitude, altitude, and time offset. This requires a minimum of four satellite measurements and involves solving a system of nonlinear equations. Modern GPS receivers use iterative numerical methods to compute position solutions, typically updating the position several times per second.

**Differential GPS (DGPS)** techniques can significantly improve positioning accuracy by using ground-based reference stations at precisely surveyed locations. These stations calculate the difference between measured and actual satellite ranges, broadcasting corrections that nearby GPS receivers can apply. The **Wide Area Augmentation System (WAAS)** used in aviation is a form of differential GPS that provides corrections via geostationary satellites.

### GPS Receiver Components and Operation

A GPS receiver consists of several key components working together to acquire satellite signals, process navigation data, and compute position solutions. The **antenna** serves as the interface between the receiver and GPS satellites, while the **processing unit** performs the complex calculations required for navigation.

The GPS antenna must be capable of receiving weak satellite signals from multiple directions simultaneously. Aviation GPS antennas are typically **omnidirectional** designs that maintain signal reception regardless of aircraft attitude. The antenna location on the aircraft is critical, requiring an unobstructed view of the sky while minimizing interference from aircraft systems and structures.

Modern GPS receivers employ **parallel processing channels**, with each channel dedicated to tracking a specific satellite. Early receivers used sequential processing, switching between satellites and requiring longer acquisition times. Current aviation GPS receivers typically feature 12 or more parallel channels, allowing simultaneous tracking of all visible satellites for optimal accuracy and reliability.

The receiver's **signal acquisition system** must first locate and lock onto GPS signals before position calculations can begin. This process involves searching for satellite signals across all possible frequency and code phase combinations. Cold start acquisition, when the receiver has no stored satellite information, can take several minutes. Warm starts with recent almanac data typically require 30-60 seconds.

> **Receiver Sensitivity**: Modern GPS receivers can track signals approximately 1,000 times weaker than early receivers, improving performance in challenging environments such as dense urban areas or under aircraft structures.

The **navigation processor** performs the mathematical calculations required to convert satellite range measurements into position solutions. This includes applying corrections for satellite clock errors, atmospheric delays, and relativistic effects. The processor also maintains the navigation database containing waypoints, airports, airspace boundaries, and other aeronautical information.

GPS receivers incorporate various **integrity monitoring** features to detect and alert users to potential navigation errors. **Receiver Autonomous Integrity Monitoring (RAIM)** uses redundant satellite measurements to check for consistency and detect satellite malfunctions. When five or more satellites are available, RAIM can both detect and exclude faulty satellites from position calculations.

The **user interface** presents navigation information in formats useful for aviation applications. This includes current position, ground track, ground speed, distance and bearing to waypoints, and estimated time of arrival. Many GPS receivers provide moving map displays showing the aircraft's position relative to airports, airspace, and terrain features.

**Database management** represents a critical aspect of GPS receiver operation in aviation applications. The navigation database must be updated regularly to reflect changes in waypoint coordinates, airspace boundaries, and instrument approach procedures. Database updates are typically required every 28 days for IFR-certified GPS receivers, ensuring pilots have access to current aeronautical information for safe flight operations.

---

## GPS ACCURACY AND ERROR SOURCES

While GPS provides remarkable positioning capabilities for aviation navigation, pilots must understand that the system is subject to various sources of error that can affect accuracy. These errors stem from the GPS constellation itself, signal propagation through the atmosphere, geometric considerations, and intentional limitations. Understanding these error sources is crucial for safe navigation and proper interpretation of GPS-derived position information.

Modern GPS receivers typically achieve horizontal accuracy within 3-5 meters under standard conditions. However, this accuracy can be degraded by several factors that pilots should recognize and account for during flight planning and navigation operations.

### Inherent GPS System Errors

**Satellite clock errors** represent one of the most significant sources of GPS inaccuracy. Each GPS satellite contains multiple atomic clocks that must maintain extremely precise timing, as even microsecond errors translate to significant position errors on the ground. A timing error of just one microsecond results in a range error of approximately 300 meters.

The GPS control segment continuously monitors satellite clock performance and uploads correction data to each satellite. However, small residual clock errors remain after these corrections are applied. These errors typically contribute 1-2 meters of range error to distance measurements between the receiver and individual satellites.

**Ephemeris errors** occur when the satellite's actual position differs from the predicted orbital position transmitted in the navigation message. The GPS control segment tracks satellite orbits and predicts their positions, but gravitational perturbations from the sun, moon, and Earth's irregular mass distribution cause small deviations from predicted paths.

These orbital prediction errors are typically most pronounced when satellites are furthest from the monitoring stations of the control segment. Ephemeris errors generally contribute 1-3 meters of ranging error and are more significant for satellites that have not received recent orbital updates from the control segment.

**Satellite hardware malfunctions** can introduce errors in signal transmission or timing. While the GPS system includes extensive monitoring to detect and exclude faulty satellites, brief periods may occur before a malfunctioning satellite is identified and marked unhealthy. Modern GPS receivers incorporate **Receiver Autonomous Integrity Monitoring (RAIM)** algorithms to detect and exclude measurements from faulty satellites.

> **RAIM Alert**: GPS receivers approved for IFR navigation must provide RAIM alerting capability. When RAIM detects a satellite fault that could cause navigation errors exceeding specified limits, it alerts the pilot and may exclude the faulty satellite from navigation calculations.

### Atmospheric Interference Effects

The atmosphere significantly affects GPS signal propagation, introducing delays that translate directly into ranging errors. These atmospheric effects are among the largest contributors to GPS positioning errors.

**Ionospheric delays** occur as GPS signals pass through the ionosphere, a layer of charged particles extending from approximately 50 to 1,000 kilometers above Earth's surface. Free electrons in the ionosphere cause signal delays that vary with solar activity, time of day, season, and geographic location.

The ionosphere affects GPS L1 and L2 frequencies differently, allowing dual-frequency receivers to calculate and remove most ionospheric error. However, most aviation GPS receivers operate on L1 frequency only and must rely on modeled corrections transmitted by the satellites. These corrections typically reduce ionospheric errors from 5-15 meters to 1-3 meters.

Ionospheric activity increases during periods of high solar activity, magnetic storms, and at equatorial latitudes. Night-to-day transitions can cause rapid changes in ionospheric delay, temporarily degrading GPS accuracy. Pilots should be aware that GPS accuracy may be reduced during significant solar weather events.

**Tropospheric delays** result from signal propagation through the lower atmosphere, where water vapor and temperature variations affect signal velocity. Unlike ionospheric effects, tropospheric delays cannot be eliminated using dual-frequency measurements and must be modeled.

Standard tropospheric models account for average atmospheric conditions based on location, altitude, and season. However, local weather conditions such as high humidity, temperature inversions, or severe weather can cause actual delays to differ significantly from modeled values. These effects are most pronounced at low satellite elevation angles where signals travel through more atmosphere.

Tropospheric errors typically contribute 1-3 meters of ranging error under normal conditions but can exceed 10 meters during severe weather or when tracking low-elevation satellites.

### Satellite Geometry and Dilution of Precision

The geometric arrangement of satellites relative to the GPS receiver significantly impacts positioning accuracy through **Dilution of Precision (DOP)** effects. Even with perfect range measurements, poor satellite geometry amplifies ranging errors into larger position errors.

**Geometric Dilution of Precision (GDOP)** represents the overall geometric strength of the satellite constellation. GDOP values below 6 are considered excellent, while values above 20 indicate very poor geometry that should be avoided for critical navigation operations.

**Position Dilution of Precision (PDOP)** specifically measures how satellite geometry affects three-dimensional position accuracy. PDOP multiplies the ranging error to determine position error. For example, if ranging accuracy is 3 meters and PDOP is 2.0, the resulting position error would be approximately 6 meters.

**Horizontal Dilution of Precision (HDOP)** focuses on geometric effects on horizontal position accuracy, which is most critical for aviation navigation. HDOP values below 2.0 provide excellent horizontal accuracy, while values above 6.0 indicate marginal geometry for precision navigation.

**Vertical Dilution of Precision (VDOP)** measures geometric effects on altitude accuracy. Vertical positioning is generally less accurate than horizontal positioning due to satellite constellation geometry, as most visible satellites are above the receiver rather than distributed around the horizon.

Poor DOP conditions occur when visible satellites are clustered in one portion of the sky or when satellite elevation angles are very low. Urban environments, mountainous terrain, or aircraft attitude can mask satellites and degrade DOP values. Modern GPS receivers display current DOP values and can predict periods of poor satellite geometry.

> **DOP Planning**: Pilots should check predicted DOP values during flight planning, especially for approaches or operations requiring high navigation accuracy. Most flight planning software and GPS receivers provide DOP prediction capabilities for specific locations and times.

### Selective Availability and Intentional Degradation

**Selective Availability (SA)** was an intentional degradation of GPS accuracy implemented by the U.S. Department of Defense from 1990 to 2000. SA introduced random errors into satellite clock and ephemeris data, limiting civilian GPS accuracy to approximately 100 meters 95% of the time.

President Clinton ordered SA to be turned off on May 1, 2000, immediately improving civilian GPS accuracy from 100 meters to less than 10 meters. This improvement enabled GPS to support precision approach procedures and other critical aviation applications.

Although SA is no longer active, the capability remains in the GPS system and could theoretically be reactivated during national emergencies. However, the widespread dependence on GPS for civilian applications makes reactivation of global SA extremely unlikely.

**Regional selective availability** or localized GPS jamming remains possible in areas of military operations or national security concerns. The U.S. government publishes NOTAMs when GPS interference testing or jamming may affect civilian operations in specific geographic areas.

Modern aviation GPS systems must account for the possibility of intentional or unintentional interference. **Wide Area Augmentation System (WAAS)** and other augmentation systems provide integrity monitoring that can detect and alert pilots to GPS signal degradation from any source, including intentional interference.

The removal of SA and development of GPS augmentation systems transformed GPS from a general navigation aid into a precision navigation system capable of supporting Category I instrument approaches and other critical flight operations requiring high accuracy and integrity.

---

## RECEIVER AUTONOMOUS INTEGRITY MONITORING (RAIM)

**Receiver Autonomous Integrity Monitoring (RAIM)** represents a critical safety feature built into GPS receivers that enables them to detect and alert pilots to potentially hazardous GPS navigation errors without relying on external monitoring systems. RAIM performs continuous internal checks of the GPS constellation to ensure navigation accuracy meets required standards for safe flight operations.

RAIM operates by comparing position solutions calculated using different combinations of available satellites. When sufficient satellites are visible, the system can detect inconsistencies that indicate satellite failures, signal interference, or other errors that could compromise navigation accuracy. This autonomous monitoring capability is essential because GPS signals can be affected by various factors including satellite clock errors, atmospheric conditions, and intentional or unintentional interference.

The importance of RAIM cannot be overstated in aviation applications. Unlike ground-based navigation aids that provide immediate visual or auditory failure indications, GPS satellites operate thousands of miles above the Earth with no direct pilot oversight. RAIM serves as the pilot's primary means of detecting GPS navigation errors before they lead to dangerous navigation mistakes.

### RAIM Principles and Fault Detection

RAIM functionality is based on **redundancy** and **consistency checking** among multiple satellite signals. The system continuously calculates position solutions using different combinations of available satellites, then compares these solutions to detect inconsistencies that indicate potential errors.

The fundamental principle underlying RAIM is **over-determination** of the navigation solution. While only four satellites are theoretically required for a three-dimensional GPS position fix (three for position, one for time), RAIM requires additional satellites to provide the redundancy necessary for fault detection. With more satellites available than the minimum required, the GPS receiver can calculate multiple position solutions and identify discrepancies.

When RAIM detects an inconsistency, it indicates that one or more satellites in the constellation may be providing erroneous information. The system compares the **residuals** (differences between measured and calculated values) from each satellite against predetermined thresholds. If these residuals exceed acceptable limits, RAIM triggers an alert indicating potential navigation errors.

**Fault detection** occurs when RAIM identifies that the GPS position solution may be unreliable, but cannot isolate which specific satellite is causing the problem. In this situation, the GPS receiver alerts the pilot that GPS navigation should not be relied upon for precision navigation, but the system cannot automatically correct the error.

**Fault detection and exclusion (FDE)** represents a more advanced RAIM capability that not only detects satellite failures but can also identify and exclude the faulty satellite from the navigation solution. This allows continued GPS navigation with the remaining healthy satellites, provided sufficient satellites remain available for accurate positioning.

> **Note**: RAIM fault detection and exclusion capabilities depend heavily on satellite geometry and the number of satellites visible to the receiver. Poor satellite geometry can reduce RAIM effectiveness even when many satellites are available.

### Satellite Visibility Requirements for RAIM

RAIM operation requires specific minimum numbers of satellites to perform its monitoring functions effectively. These requirements differ based on whether the system is performing fault detection only or fault detection and exclusion.

For basic **fault detection**, RAIM requires a minimum of **five satellites** to be visible and usable by the GPS receiver. With five satellites, the receiver can calculate multiple position solutions and detect when one solution differs significantly from others, indicating a potential satellite failure or signal error. However, with only five satellites, RAIM cannot determine which specific satellite is faulty.

For **fault detection and exclusion**, RAIM requires a minimum of **six satellites**. The additional satellite provides the redundancy necessary to isolate the faulty satellite and exclude it from the navigation solution while maintaining position accuracy with the remaining satellites. This capability allows continued GPS navigation even when one satellite fails, assuming sufficient satellites remain for accurate positioning.

Satellite geometry also significantly affects RAIM performance. **Dilution of Precision (DOP)** values, particularly **Horizontal Dilution of Precision (HDOP)** and **Position Dilution of Precision (PDOP)**, must be within acceptable limits for RAIM to function properly. Poor satellite geometry (high DOP values) can prevent RAIM availability even when the minimum number of satellites is visible.

The **RAIM hole** phenomenon occurs when satellites are positioned such that removing any one satellite from the solution significantly degrades position accuracy beyond acceptable limits. In these situations, RAIM cannot provide fault detection and exclusion even with six or more satellites visible.

Specific RAIM requirements for different phases of flight may vary. **Terminal area operations** and **approaches** require more stringent RAIM performance than **en route** navigation, necessitating better satellite geometry and potentially more visible satellites.

> **Critical Point**: Pilots must verify RAIM availability before conducting GPS-dependent operations. The number of visible satellites alone does not guarantee RAIM availability—satellite geometry and signal quality are equally important factors.

### RAIM Prediction and Availability

**RAIM prediction** allows pilots to determine in advance whether RAIM will be available for their planned flight route and time. This predictive capability is essential for flight planning, particularly when GPS will be the primary means of navigation or when conducting GPS approaches at the destination airport.

Several tools are available for RAIM prediction. The **FAA RAIM Prediction website** (www.raimprediction.net) provides detailed RAIM availability forecasts for specific airports and routes. Pilots enter their planned departure and arrival airports, flight time, and aircraft equipment type to receive a prediction of RAIM availability throughout their flight.

Many **GPS receivers** include built-in RAIM prediction capabilities. These systems use current satellite almanac data to predict RAIM availability up to several hours in advance. However, these predictions may be less comprehensive than ground-based prediction services, particularly for approaches at specific airports.

**Flight planning software** and **Electronic Flight Bag (EFB)** applications often incorporate RAIM prediction tools, allowing pilots to check RAIM availability as part of their comprehensive flight planning process. These integrated tools can highlight potential RAIM outages along planned routes and suggest alternative navigation strategies.

RAIM prediction considers several factors including satellite constellation health, planned satellite maintenance, and predicted satellite geometry. **Satellite maintenance** and **satellite failures** can affect RAIM availability, making current predictions more reliable than those generated days in advance.

For **GPS approaches**, RAIM availability must be confirmed from **two hours before** to **two hours after** the planned approach time. If RAIM is not predicted to be available during this window, pilots must plan alternative approach procedures or delay their flight until RAIM availability is restored.

**NOTAM (Notice to Airmen)** information should be checked for GPS satellite outages or maintenance that could affect RAIM availability. These NOTAMs are issued when scheduled satellite maintenance or known satellite problems will impact GPS navigation accuracy or RAIM performance.

### RAIM Failure Indications and Pilot Actions

GPS receivers provide several types of **RAIM failure indications** to alert pilots when GPS navigation accuracy may be compromised. Understanding these indications and knowing the appropriate pilot responses is crucial for safe GPS navigation.

**"RAIM NOT AVAILABLE"** or **"RAIM NA"** messages indicate that insufficient satellites or poor satellite geometry prevents the receiver from performing integrity monitoring. When this message appears, pilots should not rely on GPS for primary navigation and must use alternative navigation methods.

**"INTEGRITY FAILURE"** or **"ACCURACY DEGRADED"** messages indicate that RAIM has detected a potential satellite failure or significant navigation error. This represents a more serious condition than RAIM unavailability because it suggests that the displayed GPS position may be unreliable.

**"GPS POSITION UNRELIABLE"** warnings indicate that RAIM has detected errors exceeding acceptable limits for the current phase of flight. Pilots must immediately transition to alternative navigation methods and should not use GPS for navigation until the condition is resolved.

When RAIM failure indications occur, pilots must take immediate action. **Discontinue GPS navigation** and transition to alternative navigation aids such as VOR, NDB, or pilotage. Do not attempt to continue GPS-dependent operations including GPS approaches when RAIM failures are indicated.

For aircraft conducting **GPS approaches**, RAIM failure indications require **immediate missed approach procedures** unless visual conditions allow continuation under VFR. Pilots should not attempt to continue GPS approaches without RAIM availability, as position accuracy cannot be assured.

**Alternative navigation requirements** become critical when RAIM failures occur. Pilots must have current charts and be proficient with backup navigation methods including VOR navigation, NDB procedures, and pilotage techniques. Flight planning should always include alternative navigation strategies for routes and approaches that rely primarily on GPS.

**Documentation and reporting** of RAIM failures may be required, particularly if the failure affects safety of flight or occurs during critical phases of operation. Pilots should note the time, location, and nature of RAIM failures for potential reporting to air traffic control or aircraft maintenance personnel.

> **Emergency Procedure**: If RAIM failure occurs during a GPS approach below decision altitude, execute an immediate missed approach unless visual conditions clearly allow safe continuation. Do not attempt to troubleshoot GPS problems during critical phases of flight.

Recovery from RAIM failures often occurs automatically when satellite geometry improves or failed satellites are excluded from the solution. However, pilots should verify GPS accuracy against other navigation sources before resuming GPS-dependent operations after a RAIM failure indication has cleared.

---

## WIDE AREA AUGMENTATION SYSTEM (WAAS)

The **Wide Area Augmentation System (WAAS)** represents a significant enhancement to the basic GPS navigation capability, providing improved accuracy, integrity, continuity, and availability for aviation users throughout most of North America. WAAS is a satellite-based augmentation system that corrects GPS signal errors and provides precise navigation guidance for all phases of flight, including precision approaches to appropriately equipped airports.

WAAS was developed by the Federal Aviation Administration to meet the stringent requirements for civil aviation navigation and approach procedures. The system transforms GPS from a supplemental navigation aid into a primary means of navigation capable of supporting precision approaches with vertical guidance. This capability represents a fundamental advancement in aviation navigation technology, enabling aircraft to fly precision approaches at thousands of airports that previously required expensive ground-based navigation aids.

### WAAS System Architecture and Components

The WAAS infrastructure consists of three primary components: **ground reference stations**, **master stations**, and **geostationary satellites**. This distributed architecture provides comprehensive coverage across the Continental United States (CONUS) and parts of Alaska while maintaining the high levels of accuracy and integrity required for aviation applications.

**Ground reference stations** form the foundation of the WAAS network. Approximately 38 precisely surveyed reference stations are strategically positioned across the United States and several international locations. These stations continuously monitor GPS satellite signals 24 hours a day, measuring the difference between the received GPS position and their known exact position. Each reference station is equipped with multiple GPS receivers and can simultaneously track all GPS satellites above the horizon.

The reference stations detect errors in the GPS signals caused by satellite clock drift, orbital variations, and ionospheric delays. These errors vary by geographic location and change over time, requiring continuous monitoring. Each station computes differential corrections for the GPS signals and transmits this raw correction data to the master stations via a dedicated communication network every 2.5 seconds.

**Master stations** serve as the central processing centers for the WAAS network. Two master stations, located in Fremont, California, and Atlanta, Georgia, provide redundancy and ensure continuous system operation. The master stations receive correction data from all reference stations and process this information using sophisticated algorithms to generate wide-area corrections applicable across the entire service area.

The master stations perform several critical functions. They generate integrity messages that warn users within six seconds if any GPS satellite should not be used for navigation. They create ionospheric delay models that account for signal delays as GPS transmissions pass through the Earth's ionosphere. The stations also compute precise ephemeris corrections that improve the accuracy of satellite orbital position data.

**Geostationary satellites** broadcast the WAAS corrections and integrity information to aircraft. Two geostationary satellites, positioned at 107.3° West and 133° West longitude approximately 22,300 miles above the equator, provide WAAS signal coverage. These satellites, designated as **Galaxy 15** and **Anik F1R**, transmit on the same L1 frequency as GPS satellites (1575.42 MHz) using a GPS-like signal structure.

> **WAAS Signal Structure**: WAAS geostationary satellites transmit corrections using pseudo-random noise codes similar to GPS satellites, allowing WAAS-capable receivers to process both GPS and WAAS signals simultaneously without requiring separate antennas or receivers.

The geostationary satellites receive the processed correction messages from master stations via ground uplink stations. These corrections are then formatted into a message structure compatible with GPS receivers and broadcast continuously. Each WAAS message contains differential corrections for GPS satellites, ionospheric delay parameters, integrity flags, and precise ephemeris data.

### WAAS Accuracy Improvements and Capabilities

WAAS significantly enhances GPS accuracy through multiple correction techniques. Standard GPS provides accuracy of approximately 10-15 meters (33-49 feet) under normal conditions. WAAS-corrected GPS achieves **sub-meter accuracy**, typically providing horizontal accuracy of 1-3 meters (3-10 feet) and vertical accuracy of 1-2 meters (3-7 feet) throughout the coverage area.

The accuracy improvements result from several correction mechanisms. **Differential GPS corrections** compensate for satellite clock errors, orbital inaccuracies, and selective availability (when it was active). These corrections are computed by comparing the GPS signals received at precisely surveyed reference stations with the stations' known positions.

**Ionospheric correction models** address one of the largest sources of GPS error. The ionosphere can delay GPS signals by varying amounts depending on solar activity, time of day, season, and geographic location. WAAS reference stations measure ionospheric delays across the coverage area and generate a grid-based ionospheric model. This model allows WAAS receivers to compute appropriate ionospheric corrections for their specific location and time.

**Tropospheric corrections** account for signal delays in the lower atmosphere. While smaller than ionospheric effects, tropospheric delays can still introduce several meters of error in GPS positions. WAAS modeling techniques provide corrections for these atmospheric effects.

The **integrity function** represents one of WAAS's most critical capabilities for aviation. Within six seconds of detecting a problem with any GPS satellite, WAAS broadcasts an integrity message warning users not to use that satellite for navigation. This rapid fault detection and user notification meets the stringent integrity requirements for aviation applications, including precision approaches.

WAAS enables several advanced navigation capabilities previously unavailable with basic GPS. **Localizer Performance with Vertical Guidance (LPV)** approaches provide precision approach capability with lateral and vertical guidance similar to Instrument Landing System (ILS) approaches. LPV approaches can be designed with decision heights as low as 200 feet above ground level, compared to 400-500 feet typical for non-precision approaches.

> **LPV Approach Benefits**: LPV approaches provide a 40-meter (131-foot) wide course at the runway threshold, compared to 150 meters for standard GPS approaches, allowing pilots to fly more precise approach paths in challenging weather conditions.

**Lateral Navigation/Vertical Navigation (LNAV/VNAV)** approaches provide lateral and vertical guidance with slightly less precision than LPV but still offer significant improvements over basic GPS approaches. These approaches typically support decision heights of 250-300 feet above ground level.

### WAAS Coverage Areas and Limitations

WAAS provides navigation services across a defined coverage area that includes the Continental United States, most of Alaska, parts of Canada and Mexico, and some offshore areas in the Gulf of Mexico and along both coasts. The **CONUS coverage area** extends from approximately 25°N to 55°N latitude and from 125°W to 66°W longitude, encompassing all 48 contiguous states.

**Alaska coverage** includes most of the state, with some limitations in the far northern and western regions. WAAS coverage in Alaska extends from approximately 55°N to 71°N latitude and from 175°W to 130°W longitude. This coverage supports WAAS-based approaches at numerous Alaska airports, providing critical navigation capability in a region with limited ground-based navigation aids.

Coverage quality varies within the service area due to several factors. **Reference station distribution** affects correction accuracy, with areas closer to multiple reference stations typically receiving more accurate corrections. The geometric arrangement of GPS satellites visible from specific locations influences the precision of WAAS corrections. **Ionospheric activity** can degrade WAAS performance, particularly at northern latitudes during periods of high solar activity.

Several operational limitations affect WAAS availability and performance. **Geostationary satellite visibility** requires an unobstructed view of the southern sky (in the Northern Hemisphere) to receive WAAS corrections. Aircraft operating in mountainous terrain, dense urban areas with tall buildings, or at extreme northern latitudes may experience intermittent WAAS signal reception.

**Ionospheric storms** can temporarily disrupt WAAS operations across large geographic areas. During severe space weather events, WAAS may broadcast "Do Not Use" messages for affected regions until ionospheric conditions stabilize. These events are relatively rare but can last from several hours to several days.

The system has **altitude limitations** for certain operations. While WAAS signals can be received at all normal flight altitudes, precision approach capability using LPV procedures is typically certified for use up to 18,000 feet mean sea level. Above this altitude, WAAS continues to provide enhanced GPS navigation but may not support precision approach operations.

### WAAS vs Non-WAAS Receiver Differences

The differences between WAAS-capable and non-WAAS GPS receivers extend beyond simple accuracy improvements to encompass fundamental navigation capabilities and operational procedures. Understanding these differences is essential for pilots operating in the modern aviation environment where WAAS-based procedures are increasingly common.

**WAAS-capable receivers** incorporate additional processing capabilities to decode and apply WAAS corrections. These receivers can simultaneously track GPS satellites and WAAS geostationary satellites, processing both navigation signals and correction data. The receivers contain more sophisticated algorithms for integrity monitoring and fault detection, enabling them to meet aviation's stringent navigation requirements.

Non-WAAS GPS receivers, while still valuable for basic navigation, cannot access the enhanced accuracy and integrity features of the WAAS system. These receivers rely solely on uncorrected GPS signals and lack the integrity monitoring capabilities required for precision approaches and other advanced navigation procedures.

**Approach capability** represents the most significant operational difference between WAAS and non-WAAS systems. WAAS receivers can fly LPV approaches with decision heights as low as 200 feet, providing precision approach capability at thousands of airports. Non-WAAS receivers are limited to LNAV approaches with minimum descent altitudes typically 400 feet or higher above ground level.

**Database requirements** differ between WAAS and non-WAAS systems. WAAS receivers must contain approach procedure databases that include LPV and LNAV/VNAV procedures with their associated vertical path information. These databases require more frequent updates to maintain currency with rapidly expanding WAAS-based procedure development.

> **WAAS Receiver Certification**: WAAS GPS receivers must meet Technical Standard Order (TSO) C-145/C-146 requirements for aviation use, including extensive testing for accuracy, integrity, continuity, and availability under various operating conditions.

**Integrity monitoring** capabilities distinguish WAAS from non-WAAS receivers. WAAS receivers continuously monitor the integrity of both GPS and WAAS signals, providing pilots with real-time indications of navigation system reliability. The receivers can detect and exclude faulty satellites from navigation solutions within seconds of problem identification.

**Installation requirements** for WAAS receivers often differ from non-WAAS installations. WAAS systems typically require certified antennas optimized for receiving both GPS and geostationary satellite signals. The antenna installation must provide adequate sky coverage to maintain WAAS signal reception throughout normal flight operations.

**Operational procedures** vary significantly between WAAS and non-WAAS operations. WAAS procedures require pilots to verify system operational status before conducting precision approaches. The receivers provide specific annunciations and alerts that pilots must understand and respond to appropriately. Flight manual supplements for WAAS-equipped aircraft contain detailed procedures for normal and abnormal operations that differ substantially from basic GPS procedures.

---

## GPS NAVIGATION PROCEDURES AND OPERATIONS

Modern GPS navigation has revolutionized aircraft navigation by providing precise, worldwide position information and sophisticated approach capabilities. Understanding GPS receiver operations, navigation procedures, and integration with conventional navigation aids is essential for safe and efficient flight operations under both VFR and IFR conditions.

### GPS Receiver Operation and Interface

**GPS receivers** installed in aircraft vary significantly in complexity, from basic VFR units to sophisticated **Instrument Flight Rules (IFR)** certified systems capable of conducting precision approaches. All aviation GPS receivers share common operational characteristics that pilots must understand for safe navigation.

The primary interface components include a **Control Display Unit (CDU)** or similar interface for data entry, a navigation display showing aircraft position and flight plan information, and integration with conventional flight instruments such as the **Course Deviation Indicator (CDI)** or **Horizontal Situation Indicator (HSI)**. Modern units typically feature dedicated function keys for direct access to common operations like nearest airport, flight plan modification, and navigation source selection.

**CDI sensitivity and scaling modes** represent one of the most critical aspects of GPS navigation. Unlike VOR navigation where CDI sensitivity remains constant, GPS receivers automatically adjust CDI sensitivity based on flight phase and proximity to airports. In the **enroute mode**, full-scale CDI deflection represents ±5.0 nautical miles deviation from the desired course. This relatively wide sensitivity prevents course deviations during enroute flight from causing excessive pilot workload.

As the aircraft approaches the destination airport, the GPS receiver automatically transitions to **terminal mode** when within 30 nautical miles of the airport. In terminal mode, full-scale CDI deflection represents ±1.0 nautical mile, providing increased sensitivity for maneuvering in the terminal environment. This automatic scaling occurs without pilot intervention, though pilots must be aware of when these transitions occur to properly interpret CDI indications.

> **Important**: CDI scaling transitions occur automatically based on aircraft position relative to airports and approach procedures. Pilots cannot manually override these transitions in certified IFR GPS receivers.

The **annunciator panel** or display messages provide critical information about GPS receiver status, navigation mode, and approach phase. Common annunciations include "ENR" for enroute, "TERM" for terminal, "APPR" for approach, and various alert messages such as "RAIM UNAVAILABLE" or "GPS NAV LOST."

### Waypoint Navigation and Direct-To Procedures

**Waypoint navigation** forms the foundation of GPS operations, allowing pilots to navigate precisely to any programmed position. GPS receivers store extensive databases containing thousands of waypoints, including airports, navigation aids, intersections, and user-defined waypoints. Database updates occur every 28 days and must remain current for IFR operations.

The **direct-to function** provides the most basic GPS navigation capability, allowing pilots to navigate directly to any waypoint in the database. Activating a direct-to procedure typically requires selecting the destination waypoint and confirming the navigation command. The GPS receiver then calculates the great circle course and distance to the selected waypoint, providing continuous guidance via the CDI.

When executing a direct-to procedure, the GPS receiver establishes a **desired track (DTK)** from the aircraft's present position to the selected waypoint. The CDI indicates deviations from this desired track, with the needle showing the direction to fly to return to course. Unlike VOR navigation, GPS direct-to procedures provide precise guidance regardless of distance from the waypoint, subject only to CDI scaling limitations.

**Cross-track error (XTK)** displays show the precise distance the aircraft is displaced from the desired course, typically in nautical miles and tenths. This information proves invaluable for maintaining accurate navigation and complying with airspace requirements. Maximum cross-track errors for various flight phases are specified in **Required Navigation Performance (RNP)** standards.

Flight plan navigation extends direct-to capabilities by allowing pilots to program multiple waypoints in sequence. Most GPS receivers accommodate flight plans containing numerous waypoints, with automatic sequencing from one waypoint to the next upon reaching each waypoint. Waypoint sequencing typically occurs when the aircraft passes **abeam** the waypoint or reaches a specified distance from the waypoint.

**Waypoint alerting** provides advance notification when approaching each waypoint in a flight plan. Most receivers begin alerting approximately one minute before reaching each waypoint, allowing pilots to prepare for course changes or other required actions. The alerting time may vary based on aircraft ground speed and turn radius calculations.

### GPS Approach Procedures and Requirements

GPS approach procedures represent the most sophisticated application of satellite navigation technology, enabling precision and non-precision approaches to thousands of airports worldwide. Understanding approach types, activation procedures, and operational requirements is essential for safe IFR operations.

**GPS overlay approaches** were the first GPS approach procedures approved for general aviation use. These approaches overlay existing non-precision approaches such as VOR, NDB, or RNAV approaches, providing GPS guidance to the same approach course and minimums. Overlay approaches require conventional ground-based navigation aids to remain operational as backup navigation sources.

**GPS standalone approaches** do not require underlying ground-based navigation aids and represent true GPS-only procedures. These approaches typically provide lower minimums than overlay procedures due to the superior accuracy and integrity monitoring capabilities of GPS navigation systems. Standalone approaches include **Localizer Performance with Vertical Guidance (LPV)** and **Lateral Navigation/Vertical Navigation (LNAV/VNAV)** procedures.

**Terminal and approach mode transitions** occur automatically as the aircraft progresses through various phases of flight. When conducting an approach, the GPS receiver transitions to approach mode upon receiving approach activation confirmation from the pilot. In approach mode, CDI sensitivity automatically scales to ±0.3 nautical miles full-scale deflection, providing the precision necessary for approach operations.

The final approach segment triggers additional CDI scaling, with sensitivity increasing to ±0.3 nautical miles at the **Final Approach Fix (FAF)** and further scaling to ±350 feet (approximately ±0.07 nautical miles) at the runway threshold for LPV approaches. This progressive scaling mimics **Instrument Landing System (ILS)** localizer sensitivity, providing familiar CDI behavior for pilots transitioning from conventional approaches.

**Glidepath information** is available on approaches with vertical guidance capabilities, including LPV and LNAV/VNAV procedures. The vertical guidance appears on a separate glideslope indicator, similar to ILS operations, providing a stabilized descent path to the runway. Unlike ILS glideslope signals that originate from ground-based equipment, GPS vertical guidance is computed within the receiver using **Wide Area Augmentation System (WAAS)** corrections.

Approach activation procedures vary among GPS receivers but generally require positive pilot action to activate approach mode. Many receivers provide automatic approach loading when approaching an airport with published GPS approaches, but pilots must manually activate the approach to engage approach mode CDI scaling and guidance. Approach activation typically becomes available when within 30 nautical miles of the destination airport.

> **Critical**: Approach mode must be activated before descending on any GPS approach procedure. Flying an approach in terminal mode results in inappropriate CDI scaling and potentially unsafe approach geometry.

**Missed approach procedures** are automatically loaded into GPS receivers when approach mode is activated. Upon executing a missed approach, pilots must select the missed approach procedure on the GPS receiver to receive guidance to the missed approach holding fix or alternate instructions. The receiver typically provides immediate guidance to the missed approach waypoint upon missed approach activation.

### Integration with Conventional Navigation Aids

GPS navigation systems integrate with conventional navigation aids to provide redundancy, backup navigation capability, and compliance with regulatory requirements. Understanding these integration requirements and procedures ensures safe navigation when GPS signals become unavailable or unreliable.

**Required Navigation Performance (RNP) standards** specify navigation accuracy requirements for various phases of flight and airspace operations. GPS navigation typically meets or exceeds RNP requirements, providing RNP-0.3 capability for terminal operations and RNP-0.1 for approach procedures. These performance standards ensure consistent navigation accuracy regardless of the navigation system used.

**VOR/DME backup requirements** remain in effect for many GPS operations, particularly in areas where GPS signal reliability may be compromised. Pilots must maintain proficiency in conventional navigation techniques and carry appropriate backup navigation equipment for flights in instrument meteorological conditions. The backup navigation system must be capable of completing the intended flight plan should GPS navigation become unavailable.

Navigation source selection becomes critical when operating with both GPS and conventional navigation aids installed. Most aircraft feature a **navigation source selector** allowing pilots to choose between GPS, VOR, and other navigation inputs for CDI guidance. Pilots must ensure the correct navigation source is selected for the intended navigation procedure and verify that approach procedures match the selected navigation source.

**GPS/VOR integration** provides enhanced navigation capability by combining the precision of GPS with the reliability of ground-based navigation aids. Many GPS receivers can automatically tune VOR frequencies and provide bearing information when flying GPS approaches that overlay conventional procedures. This integration ensures that backup navigation remains available throughout the approach procedure.

**DME information** from conventional distance measuring equipment can supplement GPS navigation by providing an independent distance reference to DME-equipped airports and navigation aids. Many GPS receivers display DME distances alongside GPS-derived position information, allowing pilots to cross-check navigation accuracy and maintain situational awareness.

The integration of GPS with conventional navigation systems requires careful attention to **navigation database currency** and equipment compatibility. GPS databases must remain current for IFR operations, while conventional navigation aid information must also reflect current operational status. Regular equipment checks and database updates ensure that both GPS and backup navigation systems provide accurate and reliable navigation guidance.

**Automatic switching** between GPS and conventional navigation sources may occur in some installations when GPS integrity falls below acceptable levels. These systems provide seamless transitions to backup navigation without pilot intervention, though pilots must remain aware of the navigation source in use and verify that the backup system provides adequate guidance for the current flight phase.

Training requirements for GPS navigation emphasize the importance of understanding both GPS-specific procedures and integration with conventional navigation systems. Pilots must demonstrate proficiency in GPS operations while maintaining competency in conventional navigation techniques to ensure safe flight operations across all navigation environments and equipment configurations.

---

## GPS LIMITATIONS AND REGULATORY REQUIREMENTS

Despite its remarkable capabilities and widespread adoption, GPS navigation is subject to significant limitations and regulatory requirements that pilots must understand for safe and legal operation. The Federal Aviation Administration (FAA) has established comprehensive standards to ensure GPS equipment meets stringent performance requirements, while also mandating backup navigation capabilities and operational restrictions to maintain aviation safety standards.

### IFR GPS Equipment Requirements and TSO Standards

**Technical Standard Orders (TSOs)** define the minimum performance standards that GPS equipment must meet for certificated aircraft operations. The two primary TSO standards for IFR GPS operations are **TSO-C129** and **TSO-C146**, each representing different generations of GPS technology and capabilities.

**TSO-C129** equipment represents the earlier generation of IFR-certified GPS receivers. These units provide basic GPS navigation capability but have several important limitations. TSO-C129 equipment requires **Receiver Autonomous Integrity Monitoring (RAIM)** capability to detect satellite signal failures, as these receivers cannot utilize **Wide Area Augmentation System (WAAS)** corrections. The equipment must be installed in accordance with AC 20-138, which specifies installation requirements including antenna placement, wiring standards, and integration with other aircraft systems.

For IFR operations, TSO-C129 equipment must be installed as a **supplemental navigation system** only, meaning pilots must maintain proficiency with and carry operational conventional navigation equipment for the intended route of flight. This requirement stems from the limited accuracy and integrity monitoring capabilities of these earlier systems.

**TSO-C146** equipment represents the current standard for WAAS-enabled GPS receivers. These advanced systems provide significantly enhanced accuracy, integrity, and availability compared to TSO-C129 equipment. TSO-C146 receivers can achieve lateral navigation accuracy of 3 meters (95% of the time) and vertical navigation accuracy of 4 meters when receiving WAAS corrections.

> **Installation Requirements**: All IFR GPS equipment must be installed by an appropriately rated technician in accordance with FAA-approved data. The installation must include proper antenna placement with adequate sky view, appropriate power supply connections, and integration with required aircraft systems such as annunciators and backup power sources.

TSO-C146 equipment enables **sole means navigation** for many phases of flight, including oceanic and remote area operations where conventional navigation aids are not available. However, even these advanced systems have specific operational limitations that pilots must observe.

Both TSO standards require the equipment to provide appropriate alerts and annunciations when system integrity is compromised. The **Navigation (NAV)** flag or equivalent annunciation must be clearly visible to the pilot and must activate automatically when the system cannot provide the required navigation performance for the current phase of flight.

### GPS Approach Limitations and Restrictions

GPS approach procedures are subject to numerous limitations that directly impact operational capability and safety margins. Understanding these restrictions is critical for flight planning and execution of GPS-based instrument approaches.

**WAAS approach limitations** vary by approach type and equipment capability. **Localizer Performance with Vertical Guidance (LPV)** approaches require TSO-C146 WAAS equipment and cannot be flown with TSO-C129 receivers. LPV approaches provide decision altitudes as low as 200 feet above ground level, but require continuous WAAS signal reception throughout the approach procedure.

**LNAV (Lateral Navigation)** approaches can be flown with either TSO-C129 or TSO-C146 equipment, but minimum descent altitudes are typically higher than precision approaches. LNAV approaches require RAIM availability for TSO-C129 equipment, with RAIM prediction checks mandatory during flight planning.

**Temperature limitations** affect all GPS approaches but are particularly critical for approaches with vertical guidance. Extreme cold temperatures can cause significant altitude errors when using GPS-derived vertical guidance. When temperatures are at or below charted temperature restrictions, pilots must apply cold temperature altitude corrections or may be prohibited from flying the approach entirely.

GPS approaches are prohibited when **GPS NOTAM** conditions exist that affect system availability or performance in the terminal area. These NOTAMs may restrict specific approach procedures, require increased minimums, or prohibit GPS approaches entirely at affected airports.

**Missed approach procedures** for GPS approaches have specific requirements that differ from conventional approaches. Pilots must ensure their GPS equipment can properly sequence to the missed approach segment and provide appropriate guidance. Some GPS receivers require manual activation of the missed approach procedure, while others activate automatically when reaching the missed approach point.

> **RAIM Requirements**: For TSO-C129 equipment, RAIM availability must be confirmed before departing on an IFR flight that requires GPS navigation. RAIM predictions should be checked for the estimated time of arrival plus one hour to account for potential delays.

### Required Alternate Navigation Capabilities

Regulatory requirements mandate that aircraft equipped with GPS for IFR operations maintain alternate means of navigation capability to ensure continued safe flight operations when GPS becomes unavailable or unreliable.

**Backup navigation equipment requirements** vary depending on the phase of flight and route structure. For domestic IFR operations in the conterminous United States, aircraft must carry operational conventional navigation equipment appropriate for the route to be flown. This typically includes **VOR receivers** capable of navigating via the available VOR airway system along the planned route and to the destination and alternate airports.

**Oceanic and remote area operations** have different requirements due to the lack of conventional navigation infrastructure. Aircraft approved for these operations may use GPS as the sole means of navigation, but must carry backup systems such as **Inertial Navigation Systems (INS)** or additional independent GPS receivers to provide redundancy.

The **alternate airport navigation capability** requirement mandates that pilots must be able to complete an instrument approach at their planned alternate airport using conventional navigation equipment. This means the alternate airport must have at least one published instrument approach procedure that does not require GPS, such as an **ILS, VOR, or NDB approach**.

**Route structure considerations** also impact backup navigation requirements. Pilots planning flights on **GPS-only routes** (Q-routes) must ensure they can navigate to airports with conventional approaches in case of GPS failure. The aircraft must have sufficient fuel reserves to reach such airports using conventional navigation methods.

For **RNAV routes** that specify GPS equipment requirements, loss of GPS capability may require pilots to notify ATC immediately and request vectors to conventional navigation aids or airports with non-GPS approaches. Flight crews should pre-plan alternate routing options that utilize available conventional navigation infrastructure.

### GPS NOTAMs and Operational Restrictions

**GPS Navigation NOTAMs** provide critical information about GPS system outages, testing, and performance degradation that can affect flight safety. These NOTAMs are issued through multiple sources and require careful monitoring throughout flight planning and operations.

**WAAS NOTAMs** specifically address Wide Area Augmentation System outages and performance issues. These NOTAMs may affect LPV approach availability, vertical guidance capability, or increase approach minimums at specific airports. WAAS NOTAMs are issued both for planned maintenance and unplanned system failures.

**GPS satellite constellation NOTAMs** inform pilots of satellite outages that may affect signal availability and navigation accuracy. These outages can impact RAIM availability for TSO-C129 equipment and may require pilots to delay departure or plan alternate routes and airports.

**Testing NOTAMs** are issued when military or other government agencies conduct GPS interference testing that may affect civilian GPS operations. These NOTAMs specify geographical areas and altitudes where GPS signals may be unreliable or unavailable during specified time periods.

> **NOTAM Monitoring Requirements**: Pilots must check for GPS NOTAMs during preflight planning and continue monitoring throughout the flight. GPS system status can change rapidly, and NOTAMs may be issued with minimal advance notice for unplanned outages.

**Operational restrictions** may be imposed during GPS interference events or system degradation. These restrictions can include prohibition of GPS approaches at affected airports, requirement for conventional navigation backup, or mandatory radar vectors in terminal areas where GPS navigation is compromised.

**Military GPS jamming exercises** are conducted periodically and may affect civilian GPS operations in large geographical areas. These exercises are typically announced through NOTAMs well in advance, but may cause significant operational impacts requiring alternate flight planning or postponement of GPS-dependent operations.

The **GPS Operations Center (GPS OC)** issues system-wide NOTAMs for constellation problems that affect GPS accuracy or availability on a national or regional basis. These NOTAMs may require pilots to use conventional navigation methods or postpone operations that depend on GPS performance.

Flight crews should establish procedures for monitoring GPS NOTAMs throughout the flight, as conditions can deteriorate after departure. Many modern GPS receivers provide automatic alerting for navigation system degradation, but pilots remain responsible for staying informed about system status through official NOTAM sources and air traffic control advisories.

Understanding these limitations and regulatory requirements is essential for safe GPS navigation operations. While GPS provides exceptional navigation capability, pilots must always be prepared for system failures and have the knowledge, equipment, and procedures necessary to continue safe flight using alternate navigation methods.

---

## GPS FLIGHT PLANNING AND PREFLIGHT PROCEDURES

Proper flight planning with GPS equipment requires thorough preflight preparation that extends beyond traditional VFR planning procedures. GPS systems provide exceptional navigational capabilities, but their effective use depends on current databases, adequate satellite coverage, and proper system configuration. Pilots must verify database currency, confirm RAIM availability, review GPS-specific NOTAMs, and ensure appropriate backup navigation systems are available.

The **28-day navigation database update cycle** forms the foundation of reliable GPS navigation. Unlike paper charts that remain valid for months, GPS databases require frequent updates to maintain accuracy and regulatory compliance. Understanding these requirements and incorporating proper preflight checks ensures safe and legal GPS operations.

### GPS Database Currency and Updates

GPS navigation databases contain critical information including waypoints, airways, approaches, and airspace boundaries. The **Aeronautical Information Regulation and Control (AIRAC) cycle** mandates that navigation databases be updated every 28 days to reflect changes in the National Airspace System.

Database updates occur on specific AIRAC effective dates, typically falling on Thursdays. The current database cycle dates are published in NOTAMs and are available from GPS equipment manufacturers. For example, if the current AIRAC cycle became effective on January 5, the next update cycle begins on February 2.

**Current database requirements** vary depending on the type of GPS operation. For VFR flight, databases should be current but are not legally required to be so under Part 91 operations. However, pilots should be aware that outdated databases may contain incorrect waypoint locations, deleted navigation aids, or obsolete airspace information.

For IFR GPS operations, current databases are mandatory. **TSO-C129** and **TSO-C146** GPS units used for IFR flight must have databases that are current for the intended flight. The GPS unit will display database effective dates during startup or through menu options.

Database updates are typically distributed through several methods. **Subscription services** provide regular updates via internet download, SD cards, or USB devices. Some newer GPS units support **wireless updates** when connected to aircraft Wi-Fi systems or portable hotspots. Older units may require manual updates using data cards or cables connected to a computer.

> **Database Update Planning**: Always verify database currency before departure. Plan database updates to occur before the expiration date, allowing time to resolve any update issues. Keep backup navigation methods available when operating with older database versions.

**Database validation procedures** should be performed after each update. Verify that familiar waypoints display correct coordinates and that recent airspace changes are reflected. Some GPS units provide database verification reports showing successful update completion.

Pilots should maintain records of database update dates, particularly for aircraft used in commercial operations. The **aircraft maintenance log** should reflect database update dates, and GPS manufacturers often provide update certificates for record-keeping purposes.

### RAIM Availability Checking Procedures

**Receiver Autonomous Integrity Monitoring (RAIM)** provides essential fault detection capabilities for GPS navigation. RAIM requires specific satellite geometry and minimum satellite counts to function properly. Preflight RAIM prediction ensures adequate satellite coverage for the planned flight.

**RAIM prediction tools** are available through several sources. The **FAA's RAIM prediction website** (www.raimprediction.net) provides the most comprehensive prediction service. This tool requires input of the planned route, departure time, and aircraft location to generate RAIM availability forecasts.

When using RAIM prediction websites, enter waypoints along the planned route at approximately 100-nautical-mile intervals. Include the departure airport, destination airport, and intermediate waypoints. **Input the planned departure time in UTC** and add the estimated flight duration to determine the time window for prediction.

RAIM prediction results indicate periods when RAIM will be **available**, **unavailable**, or when **satellite geometry** may be marginal. Green indicators show good RAIM availability, yellow indicates marginal conditions, and red shows RAIM unavailability. Plan alternate navigation methods for periods of poor RAIM availability.

**Handheld GPS units** and some panel-mounted units include built-in RAIM prediction capabilities. Access these functions through the GPS unit's utility or setup menus. Enter the planned departure time and destination to receive RAIM forecasts. Some units provide graphical displays showing RAIM availability throughout the flight period.

**RAIM outage NOTAMs** are issued when scheduled satellite maintenance or satellite failures will affect RAIM availability. These NOTAMs specify geographic areas and time periods affected by reduced RAIM capabilities. Check NOTAMs carefully for any GPS or satellite-related outages affecting the planned flight route.

For flights requiring **approach-level RAIM**, verify availability for at least 15 minutes before and after the planned approach time. Approach RAIM requires higher satellite geometry standards and additional satellites compared to en route navigation RAIM.

> **RAIM Backup Planning**: Always plan alternate navigation methods when RAIM availability is questionable. Traditional navigation aids, pilotage, and dead reckoning provide reliable backups when GPS signals are compromised or satellite geometry is poor.

**Real-time RAIM monitoring** occurs continuously during flight. GPS units display RAIM status through annunciator lights, status pages, or warning messages. Monitor RAIM status regularly and be prepared to use backup navigation if RAIM is lost during critical flight phases.

### GPS NOTAM Review Requirements

GPS operations require careful review of **GPS constellation NOTAMs** that affect satellite availability and system performance. These NOTAMs are issued separately from traditional navigation aid NOTAMs and require specific attention during flight planning.

**GPS constellation status** information is available through multiple sources. The **U.S. Coast Guard Navigation Center** (www.navcen.uscg.gov) provides current GPS constellation status and satellite health information. This website displays satellite outages, maintenance schedules, and constellation health status.

**GPS NOTAMs** are classified into several categories affecting different aspects of GPS operations. **GPS satellite outages** specify individual satellites that are out of service or operating in test mode. These NOTAMs include satellite vehicle numbers and effective time periods.

**WAAS NOTAMs** address Wide Area Augmentation System outages or degraded performance. These NOTAMs may affect GPS approach capabilities, particularly for precision approaches requiring WAAS service. Review WAAS NOTAMs carefully when planning flights to airports with GPS approaches.

**Military GPS testing NOTAMs** announce planned GPS signal degradation or jamming tests. These NOTAMs specify geographic areas, altitudes, and time periods where GPS performance may be degraded. Military testing can significantly impact GPS reliability over large geographic areas.

When reviewing GPS NOTAMs, pay attention to **geographic coordinates** and **altitude restrictions**. Some GPS outages only affect specific altitudes or geographic regions. Plot NOTAM areas on sectional charts to visualize coverage areas and plan alternate routes if necessary.

**GPS approach NOTAMs** may restrict or prohibit specific GPS approaches at individual airports. These NOTAMs often result from local interference sources, airport construction, or navigation aid testing. Verify GPS approach availability at the destination and alternate airports.

**Standard NOTAM sources** include Flight Service Station briefings, DUATS, and web-based briefing services. Specifically request GPS NOTAMs during briefings, as they may not be included in standard area briefings. Some briefing services require special selection of GPS NOTAM categories.

> **NOTAM Integration**: Combine GPS NOTAM information with RAIM predictions to develop comprehensive navigation planning. GPS outages shown in NOTAMs may not be reflected in RAIM prediction tools, requiring manual correlation of information sources.

### Flight Plan Filing with GPS Equipment

Flight plan filing with GPS equipment requires proper **equipment suffix codes** that communicate GPS capabilities to air traffic control. These codes inform ATC of available navigation and surveillance capabilities, affecting routing clearances and separation standards.

**Equipment suffix codes** for GPS-equipped aircraft include several options depending on installed equipment combinations. **/G** indicates GPS navigation capability without WAAS precision approach capability. **/L** designates aircraft with GPS navigation and ILS approach capabilities.

For aircraft with **WAAS-capable GPS** systems, use equipment suffix **/S** when filing IFR flight plans. This code indicates precision approach capability equivalent to ILS systems. VFR flight plans may use **/G** or **/S** codes depending on installed GPS capabilities.

**Transponder codes** must be combined with GPS equipment codes when filing flight plans. For example, **/S** indicates GPS with WAAS capability, while **/G** shows GPS without precision approach capability. Mode C transponder-equipped aircraft add these codes to the standard equipment designators.

**Flight plan route descriptions** should reflect GPS navigation capabilities while maintaining backup navigation options. File routes using GPS waypoints and airways, but ensure alternate navigation aids are available along the planned route. Include VOR stations and NDB facilities as intermediate waypoints when possible.

When filing **direct GPS routes**, consider air traffic control routing limitations and preferred routes. Some controllers may not approve direct GPS routing in congested airspace or over long distances. File reasonable GPS routes that follow general traffic flow patterns.

**RNAV (GPS) approaches** should be specified in flight plan remarks when planning GPS approaches at the destination airport. This information helps controllers provide appropriate approach clearances and routing. Include alternate approach types when filing flights to airports with limited GPS approach capabilities.

**Backup navigation requirements** must be addressed in flight planning for IFR GPS operations. While GPS primary navigation is authorized, backup navigation systems must be available and operational. File flight plans showing capability for both GPS and traditional navigation systems.

**International flight plans** using GPS equipment require coordination with destination country requirements. Some countries have specific GPS equipment approval requirements or mandate backup navigation systems. Research destination country GPS regulations before filing international flight plans.

> **Equipment Code Accuracy**: Use correct equipment suffix codes that accurately reflect installed and operational GPS capabilities. Incorrect codes may result in inappropriate ATC routing or approach clearances that exceed aircraft capabilities.

Backup navigation planning remains critical even with sophisticated GPS systems installed. Plan flights with adequate traditional navigation aids available as alternates to GPS navigation. Consider VOR stations, NDB facilities, and pilotage checkpoints along the planned route to provide navigation redundancy in case of GPS system failures or signal degradation.

---

## GPS TROUBLESHOOTING AND EMERGENCY PROCEDURES

GPS systems, while highly reliable, can experience failures that require immediate pilot recognition and appropriate response. Understanding common failure modes, proper emergency procedures, and backup navigation methods is essential for flight safety. This section covers systematic troubleshooting approaches, emergency navigation procedures, and the critical transition to conventional navigation systems when GPS becomes unavailable.

### Common GPS Failure Modes and Indications

GPS receivers provide various **annunciations** and **warning flags** to alert pilots of system malfunctions or degraded performance. Understanding these indications is crucial for determining the appropriate response and whether continued navigation is safe.

The most common GPS failure indication is the **integrity flag** or **NAV flag**, which appears when the receiver cannot guarantee position accuracy within acceptable limits. This flag may appear due to insufficient satellite coverage, poor satellite geometry, or receiver malfunction. When this flag is displayed, GPS navigation should not be used for primary navigation.

**Loss of RAIM** (Receiver Autonomous Integrity Monitoring) capability is indicated by specific annunciations such as "RAIM NOT AVAILABLE" or "INTEGRITY NOT AVAILABLE." Without RAIM, the GPS receiver cannot detect satellite failures that could cause hazardous navigation errors. For IFR operations, RAIM availability is mandatory, and its loss requires immediate action.

**Satellite signal loss** manifests through decreasing signal strength indicators and eventual loss of position updates. Modern GPS receivers typically display the number of satellites being tracked and their signal strength. A sudden drop to fewer than four satellites results in loss of 3D navigation capability.

**Database currency warnings** alert pilots when the navigation database has expired or contains outdated information. Messages like "DATABASE EXPIRED" or "WAYPOINT NOT IN DATABASE" indicate the need for database updates. Expired databases should not be used for IFR navigation.

> **Critical Alert**: Never ignore GPS warning flags or annunciations. When in doubt about GPS integrity, immediately revert to backup navigation methods and inform ATC of your navigation status.

**CDI scaling failures** occur when the Course Deviation Indicator does not properly transition between en route (±5 nautical miles full scale) and approach scaling (±0.3 nautical miles for LPV approaches). Improper scaling can lead to significant navigation errors during approach phases.

**Position jumping** or erratic navigation displays indicate potential multipath interference, where GPS signals reflect off terrain or structures before reaching the receiver. This is most common in mountainous areas or near large structures and typically resolves when clear of the interference source.

### Loss of GPS Navigation Procedures

When GPS navigation becomes unavailable or unreliable, pilots must quickly assess the situation and implement appropriate backup procedures. The response depends on flight phase, weather conditions, and available backup navigation equipment.

**Immediate Actions** upon GPS failure include maintaining aircraft control, noting current position from the last reliable GPS indication, and checking backup navigation equipment. If operating under IFR, inform ATC immediately of the GPS failure and request radar vectors or alternative navigation guidance.

**En Route GPS Loss** procedures vary based on flight rules and conditions. For VFR flights with adequate visibility, revert to pilotage and dead reckoning navigation. Identify prominent landmarks from the sectional chart and establish your approximate position. Maintain heading toward your destination while using visual checkpoints for navigation confirmation.

For IFR flights experiencing GPS loss, immediately contact ATC and report "GPS FAILURE" along with your position and request. ATC can provide radar vectors to your destination or to a facility equipped with conventional navigation aids. If radar coverage is unavailable, you may need to execute the lost communications procedures outlined in 14 CFR 91.185.

**Navigation Database Failures** require specific responses depending on the type of operation. If the database becomes corrupted or unavailable during flight, the GPS receiver may revert to a basic mode with limited functionality. Terminal procedures and approach navigation may be unavailable, requiring use of conventional navigation aids for arrival and approach.

**Partial GPS Degradation** situations, where GPS remains functional but with reduced accuracy, require careful evaluation. Check RAIM predictions and current satellite geometry. If operating IFR, consider requesting radar vectors or transitioning to conventional navigation aids before GPS accuracy degrades further.

### GPS Approach Missed Approach Procedures

GPS approach failures require immediate recognition and execution of published missed approach procedures. The critical factor is determining whether the failure allows completion of the approach or mandates immediate missed approach execution.

**Pre-Approach GPS Failures** occurring before the final approach fix (FAF) typically require abandoning the GPS approach and requesting vectors for an alternative approach. If the airport has conventional navigation aids, request an ILS, VOR, or NDB approach as appropriate for available equipment.

**GPS Failure During Approach** after passing the FAF presents a more complex situation. If the failure occurs before the missed approach point (MAP) and visual references are not established, execute the published missed approach procedure immediately. Use the last known GPS position to estimate your location on the approach course.

**WAAS Signal Loss** during precision approaches (LPV or LNAV/VNAV) requires immediate assessment of approach continuation criteria. If the approach downgrades to LNAV minimums and you can comply with those minimums, continue the approach. If not, execute the missed approach procedure.

The **missed approach procedure** for GPS approaches follows the published routing in the approach chart. However, with GPS failure, navigation during the missed approach may require radar vectors or use of backup navigation equipment. Inform ATC immediately of the GPS failure and request appropriate guidance.

**Approach Mode Annunciations** provide critical information about GPS approach status. "APPROACH NOT LOADED," "APPROACH INACTIVE," or similar messages indicate the GPS is not properly configured for approach navigation. These conditions require immediate attention and typically mandate a missed approach if occurring during critical phases of flight.

> **Safety Note**: GPS approach procedures assume normal GPS operation throughout the approach. Any GPS failure or warning during approach phases should be treated as a serious emergency requiring immediate action and ATC coordination.

### Reverting to Conventional Navigation Methods

When GPS becomes unavailable, pilots must efficiently transition to backup navigation systems. This transition requires familiarity with conventional navigation aids and proper procedures for their use.

**VOR Navigation Transition** involves tuning appropriate VOR frequencies, identifying stations, and establishing position relative to VOR radials. Use sectional charts to identify nearby VOR stations and their frequencies. Set the OBS to determine your radial from the station and establish a course toward your destination or an appropriate navigation fix.

**NDB Navigation** using Automatic Direction Finding (ADF) equipment provides basic directional guidance when GPS fails. Tune the appropriate NDB frequency, identify the station, and use relative bearing information to establish navigation tracking. Remember that ADF indicates relative bearing to the station, not magnetic bearing.

**Pilotage and Dead Reckoning** become primary navigation methods when electronic navigation aids are unavailable. Use visual landmarks, roads, rivers, and prominent terrain features for position confirmation. Calculate time and distance to destination based on groundspeed and magnetic heading, accounting for wind drift.

**Communication Navigation** involves using ATC radar services for navigation guidance. Request "radar vectors" to your destination when conventional navigation aids are not available. Provide ATC with your current position, heading, and altitude to facilitate radar identification and guidance.

**Chart Supplement and Navigation Planning** information becomes critical during GPS failures. Refer to the Chart Supplement U.S. (formerly Airport/Facility Directory) for alternative navigation aid frequencies, airport information, and communication procedures at your destination airport.

**Emergency Navigation Equipment** such as handheld GPS units, tablet computers with GPS capability, or smartphone navigation apps can provide backup navigation capability. However, these devices should supplement, not replace, proper conventional navigation procedures and should not be relied upon for IFR navigation.

The transition to conventional navigation requires quick decision-making and systematic execution. Practice these procedures regularly to maintain proficiency, as GPS failures often occur during high-workload phases of flight when efficient response is most critical. Always inform ATC of navigation capability changes and request assistance as needed to ensure safe flight continuation.

## Summary

Review the key points from this unit:

- GPS operates using a constellation of at least 24 satellites in Medium Earth Orbit that provide global navigation coverage 24 hours a day in all weather conditions.
- GPS positioning relies on trilateration, measuring the time for signals to travel from satellites to determine precise aircraft position using signals from at least four satellites.
- GPS satellites transmit signals on L1 (1575.42 MHz) and L2 (1227.60 MHz) frequencies, with civilian aviation using the C/A code on L1 for standard navigation operations.
- GPS accuracy is affected by satellite clock errors, atmospheric delays (ionospheric and tropospheric), satellite geometry, and ephemeris errors, typically achieving 3-5 meter horizontal accuracy.
- Dilution of Precision (DOP) values indicate how satellite geometry affects positioning accuracy, with lower values providing better accuracy and HDOP being most critical for aviation.
- Receiver Autonomous Integrity Monitoring (RAIM) provides fault detection by comparing position solutions from different satellite combinations to identify navigation errors.
- RAIM requires a minimum of five satellites for fault detection and six satellites for fault detection and exclusion capabilities.
- RAIM availability must be predicted and confirmed before GPS-dependent operations, especially for approaches requiring verification two hours before and after planned times.
- Selective Availability was discontinued in 2000, significantly improving civilian GPS accuracy from 100 meters to less than 10 meters.

---

## Key Terms

| Term | Definition |
|------|------------|
| **Trilateration** | Mathematical principle used by GPS to determine position by measuring distances to three or more satellites with known positions |
| **Ephemeris Data** | Orbital parameters broadcast by GPS satellites that describe their precise positions, updated regularly and valid for approximately four hours |
| **C/A Code** | Coarse/Acquisition code transmitted on L1 frequency for civilian GPS use, repeating every millisecond to provide ranging information |
| **RAIM** | Receiver Autonomous Integrity Monitoring - internal GPS receiver function that detects navigation errors by comparing multiple satellite solutions |
| **Pseudorange** | Distance measurement from GPS receiver to satellite that includes both actual range and clock errors from satellite and receiver timing differences |
| **GDOP** | Geometric Dilution of Precision - measure of how satellite geometry affects overall positioning accuracy, with lower values indicating better geometry |
| **HDOP** | Horizontal Dilution of Precision - specific measure of how satellite geometry affects horizontal position accuracy, most critical for aviation navigation |
| **Ionospheric Delay** | Signal propagation delay caused by charged particles in the ionosphere, varying with solar activity and contributing 1-15 meters of ranging error |
| **Selective Availability** | Intentional GPS accuracy degradation implemented by DoD from 1990-2000, limiting civilian accuracy to approximately 100 meters |
| **Fault Detection and Exclusion** | Advanced RAIM capability that identifies and removes faulty satellites from navigation calculations while maintaining position accuracy |
| **Medium Earth Orbit** | GPS satellite orbital altitude of approximately 12,550 nautical miles, providing optimal coverage and signal strength for global navigation |
| **Constellation** | Complete network of GPS satellites arranged in six orbital planes with four satellites per plane, ensuring global coverage |
| **WAAS** | Wide Area Augmentation System - differential GPS system that provides corrections and integrity monitoring for precision approach operations |

---

## Review Questions

**Multiple Choice**

1. What is the minimum number of satellites required for GPS three-dimensional positioning?
   - A) Three satellites
   - B) Four satellites
   - C) Five satellites
   - D) Six satellites

2. GPS satellites orbit Earth at approximately what altitude?
   - A) 6,200 nautical miles
   - B) 10,900 nautical miles
   - C) 12,550 nautical miles
   - D) 22,300 nautical miles

3. What does RAIM require for fault detection and exclusion capability?
   - A) Four satellites minimum
   - B) Five satellites minimum
   - C) Six satellites minimum
   - D) Seven satellites minimum

4. The GPS L1 frequency operates at:
   - A) 1227.60 MHz
   - B) 1575.42 MHz
   - C) 1090 MHz
   - D) 978 MHz

**True/False**

5. GPS satellites complete one orbit around Earth every 24 hours.
   **Answer: False** (GPS satellites orbit every 12 hours)

6. Selective Availability was permanently discontinued on May 1, 2000.
   **Answer: True**

7. Ionospheric delays affect GPS L1 and L2 frequencies equally.
   **Answer: False** (Different frequencies are affected differently)

8. HDOP values below 2.0 indicate excellent horizontal positioning geometry.
   **Answer: True**

**Short Answer**

9. Explain why GPS requires atomic clocks and how timing errors affect position accuracy.

10. Describe the difference between fault detection and fault detection and exclusion in RAIM operations.

**Matching**

11. Match the GPS error source with its typical magnitude:
    - Satellite clock errors → 1-2 meters
    - Ionospheric delays → 1-3 meters (after correction)
    - Tropospheric delays → 1-3 meters
    - Ephemeris errors → 1-3 meters

12. For GPS approaches, RAIM availability must be confirmed during what time period relative to the planned approach time?
    **Answer: From two hours before to two hours after the planned approach time**

---

## FAA References

- PHAK Chapter 16: Navigation, GPS Navigation section
- AIM Chapter 1: Air Navigation, Section 1-1-17 through 1-1-22
- AC 90-105A: Approval Guidance for RNP Operations and Barometric Vertical Navigation in the U.S. National Airspace System