//
//  OtherViewController.swift
//  Segue
//
//  Created by MJ Norona on 7/7/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class OtherViewController: UIViewController {

    @IBOutlet weak var outputLabel: UILabel!
    
    var output: String?
    override func viewDidLoad() {
        super.viewDidLoad()
        outputLabel.text = output
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
        outputLabel.text = output
    }
    

    @IBAction func dismissButtonPressed(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
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
