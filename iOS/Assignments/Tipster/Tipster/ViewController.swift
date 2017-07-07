//
//  ViewController.swift
//  Tipster
//
//  Created by MJ Norona on 7/6/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var inputString: String = ""
    var inputValue: Double = 0
    var decimal = false
    var tip1Percentage: Double = 0.5
    var tip2Percentage: Double = 0.10
    var tip3Percentage: Double  = 0.15
    var groupSize: Double = 1

    @IBOutlet weak var inputLabel: UILabel!
    
    @IBOutlet weak var percent1Label: UILabel!
    @IBOutlet weak var percent2Label: UILabel!
    @IBOutlet weak var percent3Label: UILabel!
    
    @IBOutlet weak var tip1Label: UILabel!
    @IBOutlet weak var tip2Label: UILabel!
    @IBOutlet weak var tip3Label: UILabel!
    
    @IBOutlet weak var result1Label: UILabel!
    @IBOutlet weak var result2Label: UILabel!
    @IBOutlet weak var result3Label: UILabel!
    
    @IBOutlet weak var groupLabel: UILabel!
    
    
    //number buttons
    @IBAction func numberButtonPressed(_ sender: UIButton) {
        inputString += String(sender.tag)
        inputValue = Double(inputString)!
        print(inputValue)
        
        updateLabels()
        
        inputLabel.text = inputString
    }
    
    @IBAction func clearButtonPressed(_ sender: UIButton) {
        inputString = ""
        inputValue = 0
        decimal = false
        print(inputValue)
        
        updateLabels()
        inputLabel.text = String(0)
    }
    
    @IBAction func decimalButtonPressed(_ sender: UIButton) {
        if !decimal{
            decimal = true
            inputString += "."
            inputLabel.text = inputString
        }
        
    }
    
    
    
    //sliders
    @IBAction func tipSliderChanged(_ sender: UISlider) {
        let slideValue = lround(Double(sender.value))
        //set tip percentage
        tip1Percentage = Double(slideValue) * 0.01
        tip2Percentage = Double(slideValue + 5) * 0.01
        tip3Percentage = Double(slideValue + 10) * 0.01
        
        
        //set label percentage
        percent1Label.text = ("\(slideValue)%")
        percent2Label.text = ("\(slideValue + 5)%")
        percent3Label.text = ("\(slideValue + 10)%")
        
        updateLabels()
    }
    
    
    @IBAction func groupSliderChanged(_ sender: UISlider) {
        groupSize = Double(lround(Double(sender.value)))
        groupLabel.text = "Group Size: \(Int(groupSize))"
        updateLabels()
    }
    
    func updateLabels() {
        let tip1 = (inputValue * tip1Percentage)/groupSize
        let tip2 = (inputValue * tip2Percentage)/groupSize
        let tip3 = (inputValue * tip3Percentage)/groupSize
        
        //reset tip values
        tip1Label.text = String(format: "%.2f", tip1)
        tip2Label.text = String(format: "%.2f", tip2)
        tip3Label.text = String(format: "%.2f", tip3)
        
        //reset result values
        result1Label.text = String(format: "%.2f", (tip1 + inputValue))
        result2Label.text = String(format: "%.2f", (tip2 + inputValue))
        result3Label.text = String(format: "%.2f", (tip3 + inputValue))
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        inputLabel.text = String(0)
        percent1Label.text = "5%"
        percent2Label.text = "10%"
        percent3Label.text = "15%"
        tip1Label.text = "0.00"
        tip2Label.text = "0.00"
        tip3Label.text = "0.00"
        result1Label.text = "0.00"
        result2Label.text = "0.00"
        result3Label.text = "0.00"
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
        
    }


}

