//
//  ViewController.swift
//  MapsTest
//
//  Created by MJ Norona on 7/13/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit
import GoogleMaps

class ViewController: UIViewController {
    
    override func loadView() {
        navigationItem.title = "Hello Map"
        
        let camera = GMSCameraPosition.camera(withLatitude: -33.868,
                                              longitude: 151.2086,
                                              zoom: 14)
        let mapView = GMSMapView.map(withFrame: .zero, camera: camera)
        
        let marker = GMSMarker()
        marker.position = camera.target
        marker.snippet = "Hello World"
        marker.appearAnimation = kGMSMarkerAnimationPop
        marker.map = mapView
        
        view = mapView
    }
}

