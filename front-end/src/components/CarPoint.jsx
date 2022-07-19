import React from "react";
import { Marker, Popup, Polyline } from "react-leaflet";
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

  const polyline = [
    [52.22635, 20.944347],
    [52.22647, 20.945171],
    [52.22668, 20.946463],
    [52.22686, 20.947567],
    [52.22703, 20.948666],
    [52.22726, 20.949955],
    [52.227398, 20.950785],
    [52.22815, 20.962015],
    [52.228188, 20.962646],
    [52.22821, 20.963121],
    [52.228374, 20.966059],
  ];

  const fillBlueOptions = { fillColor: "blue" };
  const purpleOptions = { color: "purple" };

  return (
    locations.length > 0 &&
    locations.map(({ latlng }, index) => (
      <>
        <Marker position={latlng} icon={pausedIcon} key={index}>
          <Popup>
            This is stopped car <br /> Car's Number is 1030
          </Popup>
        </Marker>
        <Polyline pathOptions={purpleOptions} positions={polyline} />
      </>
    ))
  );
}
