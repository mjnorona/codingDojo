//
//  ViewController.swift
//  Cold Call
//
//  Created by MJ Norona on 7/5/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var names = ["MJ", "Jazz", "Marc", "Gemma", "Paciencia"]
    
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var numberLabel: UILabel!
    
    
    @IBAction func coldButtonPressed(_ sender: Any) {
        let randName = Int(arc4random_uniform(5))
        let randNumber = Int(arc4random_uniform(5) + 1)
        updateUI(index: randName, number: randNumber)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        numberLabel.isHidden = true
    }

    func updateUI(index: Int, number: Int) {
        nameLabel.text = names[index]
        numberLabel.text = String(number)
        if number <= 2 {
            numberLabel.textColor = UIColor.red
        }
        else if number == 3 || number == 4 {
            numberLabel.textColor = UIColor.orange
        }
        else {
            numberLabel.textColor = UIColor.green
        }
        numberLabel.isHidden = false
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

