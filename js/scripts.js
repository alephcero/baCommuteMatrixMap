function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}

function getColor(d) {
        return  d >= 53.6  ? '#ca0020' :
        d >= 38.7  ? '#f4a582' :
        d >= 29.9  ? '#f7f7f7' :        
        d >= 21.65  ? '#92c5de' :
        d >= 0 ? '#0571b0' :
        //if none
    '#FFFFFF';
}

