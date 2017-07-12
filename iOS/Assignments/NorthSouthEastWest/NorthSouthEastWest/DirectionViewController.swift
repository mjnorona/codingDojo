//
//  DirectionViewController.swift
//  NorthSouthEastWest
//
//  Created by MJ Norona on 7/11/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class DirectionViewController: UIViewController {

    @IBOutlet weak var Direction: UIButton!
    var output: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        Direction.setTitle(output, for: .normal)
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
