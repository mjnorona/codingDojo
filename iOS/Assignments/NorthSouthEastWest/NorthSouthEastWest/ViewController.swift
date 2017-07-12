//
//  ViewController.swift
//  NorthSouthEastWest
//
//  Created by MJ Norona on 7/11/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBAction func directionButtonPressed(_ sender: UIButton) {
        performSegue(withIdentifier: "Segue", sender: sender)
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let directionTableViewController = segue.destination as! DirectionViewController
        var type = (sender is UIButton ? true : false)
        if type == true {
            let newSend = sender as! UIButton
            directionTableViewController.output = newSend.currentTitle
        }
        
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func unwindToVC1(segue:UIStoryboardSegue) { }
    
    


}

