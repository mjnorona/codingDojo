//
//  PersonDescriptionViewController.swift
//  Star Wars Encyclopedia
//
//  Created by MJ Norona on 7/17/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class PersonDescriptionViewController: UIViewController {
    var name = ""
    var gender = ""
    var birth = ""
    var mass = ""
    
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var genderLabel: UILabel!
    @IBOutlet weak var birthLabel: UILabel!
    @IBOutlet weak var massLabel: UILabel!
   
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        nameLabel.text = "Name: \(name)"
        genderLabel.text = "Gender: \(gender)"
        birthLabel.text = "Birth Year: \(birth)"
        massLabel.text = "Mass: \(mass)"
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
