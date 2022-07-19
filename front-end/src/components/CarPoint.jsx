import React from "react";
import { Marker, Popup } from "react-leaflet";
import L from "leaflet";

export default function CarPoint(props) {
  const locations = props.locations;
  const pausedIcon = L.icon({
    iconUrl: "./paused-car.png",

    iconSize: [20, 40], // size of the icon
  });

  const movingIcon = L.icon({
    iconUrl: "./normal-car.png",

    iconSize: [20, 40], // size of the icon
  });

  return (
    locations.length > 0 &&
    locations.map(({ latlng }, index) => (
      <Marker position={latlng} icon={pausedIcon} key={index}>
        <Popup>
          This is stopped car <br /> Car's Number is 1030
        </Popup>
      </Marker>
    ))
  );
}
