import { useState } from "react";
import { useMapEvents } from "react-leaflet";
import CarPoint from "./CarPoint";

function LocationMarkers() {
  const [locations, setLocations] = useState(
    [
      {
        latlng: [52.22635, 20.944347],
        name: "point1",
        caseStatus: "random point1"
      }
    ],
  );

  useMapEvents({
    dblclick(ev) {
      const { lat, lng } = ev.latlng;
      const newLocations = [...locations];
      newLocations.push({ latlng: [lat, lng], name: "", caseStatus: "" });
      setLocations(newLocations);
    }
  });

  return <CarPoint locations={locations} />;
}

export default LocationMarkers;
