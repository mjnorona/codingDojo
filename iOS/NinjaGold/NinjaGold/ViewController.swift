//
//  ViewController.swift
//  NinjaGold
//
//  Created by MJ Norona on 7/5/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var score: Int = 0

    @IBOutlet weak var scoreLabel: UILabel!
    @IBOutlet weak var farmLabel: UILabel!
    @IBOutlet weak var caveLabel: UILabel!
    @IBOutlet weak var houseLabel: UILabel!
    @IBOutlet weak var casinoLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        farmLabel.isHidden = true
        caveLabel.isHidden = true
        houseLabel.isHidden = true
        casinoLabel.isHidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    
    @IBAction func buildingButtonPressed(_ sender: UIButton) {
        var farm = false
        var cave = false
        var house = false
        var casino = false
        
        if sender.tag == 1{
            let rand = Int(arc4random_uniform(11) + 10)
            score += rand
            farm = true
            farmLabel.text = ("You earned \(rand)")
        } else if sender.tag == 2 {
            let rand = Int(arc4random_uniform(6) + 5)
            score += rand
            cave = true
            caveLabel.text = ("You earned \(rand)")
        } else if sender.tag == 3 {
            let rand = Int(arc4random_uniform(4) + 2)
            score += rand
            house = true
            houseLabel.text = ("You earned \(rand)")
        } else {
            let rand = Int(arc4random_uniform(51))
            let randTake = Int(arc4random_uniform(2))
            casino = true
            if randTake == 0 {
                score -= rand
                casinoLabel.text = ("You lost \(rand)")
            } else {
                score += rand
                casinoLabel.text = ("You earned \(rand)")
            }
        }
        
        if farm == true {
            farmLabel.isHidden = false
            caveLabel.isHidden = true
            houseLabel.isHidden = true
            casinoLabel.isHidden = true
        } else if cave == true {
            farmLabel.isHidden = true
            caveLabel.isHidden = false
            houseLabel.isHidden = true
            casinoLabel.isHidden = true
        } else if house == true {
            farmLabel.isHidden = true
            caveLabel.isHidden = true
            houseLabel.isHidden = false
            casinoLabel.isHidden = true
        } else {
            farmLabel.isHidden = true
            caveLabel.isHidden = true
            houseLabel.isHidden = true
            casinoLabel.isHidden = false
        }
        scoreLabel.text = String(score)
    }
    
    @IBAction func resetButtonPressed(_ sender: UIButton) {
        score = 0
        scoreLabel.text = String(score)
    }
    

}

