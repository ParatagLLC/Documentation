# Paratag User Manual

---

## Legal Disclaimer

Skydiving is an inherently dangerous activity. Mounting any device to a parachute system introduces additional risk. It is the sole responsibility of the jumper and the rigger of the parachute system to assess whether mounting a Paratag is appropriate for their equipment and jump conditions. The manufacturers of Paratag accept no liability for injury, death, or equipment damage arising from use or misuse of this device.

---

## Paratag Overview

Paratag is a small GPS transmitter designed to be mounted on a skydiving rig. It transmits its position over radio to a ground receiver, which relays the data to a phone app and cloud server in real time.

<div align="center">
  <a href="https://www.youtube.com/playlist?list=PLRnppc4hiiLs" title="Paratag How-To Guide — Watch on YouTube">
    <img src="https://i.ytimg.com/vi/LNZTzKj6ZiU/hqdefault.jpg" alt="Paratag How-To Guide" width="480"><br>
    ▶&nbsp;Watch the How-To Guide on YouTube
  </a>
</div>

### Mounting

<!-- TODO: describe recommended mounting location on the rig, hardware required, TSO/PMA considerations -->

### Using the Buttons

<!-- TODO: describe button functions (power on, pairing mode, etc.) -->

### LEDs

| Pattern | Meaning |
|---------|---------|
| Half on / half off (blue) | Pairing mode |
| <!-- TODO --> | <!-- TODO --> |

---

## App

Two companion apps exist:

- **Paratag Groundstation** — Android
- **Paratag** — iOS

Both of these apps are designed to listen to Paratag radio traffic and relay it to the Paratag server.

Screenshots below are from both apps.

### Creating a Paratag Account / Signing In

<!-- TODO -->

### Connecting to the Bluetooth Receiver

The app connects to a receiver over Bluetooth.

![Paratag receiver](images/paratag_receiver.jpg)

<!-- TODO: describe how to pair the phone to the receiver for the first time -->

<div style="display:flex; gap:8px;">
  <img src="images/groundstation_app_bluetooth.png" width="200" alt="Bluetooth scan screen">
</div>

### Pairing a New Paratag via the App

1. Turn on the Paratag (like an AAD).
2. Hold the button until the LED flashes blue (half on / half off) — this is pairing mode.
3. In the app, open **Pair New Device** and tap **SEND PAIRING REQUEST**.
4. Repeat until the app confirms pairing succeeded.

![Pairing screen](images/groundstation_app_pairing.png)

### Register a Paired Paratag to Your Account

Visit https://app.flyparatag.com/#/registerdevice to begin registering a paratag to your account. It will ask you about a Paratag ID. This is the unique identifier number assigned to your Paratag, and will appear in your app

![Register your Paratag](images/register_webapp.png)

After pairing, open the device detail screen and tap **REGISTER PARATAG** (Android) or **Register to account** (iOS) to associate the beacon with your online account.

<div style="display:flex; gap:8px;">
  <img src="images/groundstation_app_device_details.png" width="200" alt="Android device details">
  <img src="images/iOS_app_device_details.png" width="200" alt="iOS device details">
</div>

### Seeing All Paratag Devices

The main screen lists your paired beacons, other beacons heard by the receiver, and the receiver itself. Each card shows the last-seen time, battery level, and current state.

![Main device list](images/iOS_app_devices.png)

### Device Details Screen

Tapping a device shows its last known GPS position, altitude, rate of ascent, state, flash memory usage, firmware version, and configurable parameters (power level, auto-shutdown timer).

---

## Website

<!-- TODO: URL for the Paratag web portal -->

### Jump Logs

<!-- TODO: describe how completed jumps appear in the web portal, filtering, export -->

### Live Streaming Jump Data

<!-- TODO: describe real-time tracking view during an active jump -->


