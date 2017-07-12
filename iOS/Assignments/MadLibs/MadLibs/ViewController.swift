//
//  ViewController.swift
//  MadLibs
//
//  Created by MJ Norona on 7/11/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var madLibsLabel: UILabel!
    var sentence: String?
    var first:String?
    var second: String?
    var third: String?
    var fourth: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        madLibsLabel.text = sentence
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
    }
    
    @IBAction func unwindToVC1(segue:UIStoryboardSegue) {
        let formViewController = segue.source as! FormViewController
        first = formViewController.firstLabel.text
        second = formViewController.secondLabel.text
        third = formViewController.thirdLabel.text
        fourth = formViewController.fourthLabel.text
        sentence = "We are having a perfectly \(first!) time now. Later we will \(second!) and \(third!) in the \(fourth!)"
        madLibsLabel.text = sentence
        
    }

}

