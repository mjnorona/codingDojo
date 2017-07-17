//
//  FilmDescriptionViewController.swift
//  Star Wars Encyclopedia
//
//  Created by MJ Norona on 7/17/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class FilmDescriptionViewController: UIViewController {
    
    var film = ""
    var releaseDate = ""
    var director = ""
    var opening = ""

    
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var releaseDateLabel: UILabel!
    @IBOutlet weak var directorLabel: UILabel!
    @IBOutlet weak var openingLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        titleLabel.text = "Title: \(film)"
        releaseDateLabel.text = "Release Date: \(releaseDate)"
        directorLabel.text = "Director: \(director)"
        openingLabel.text = "Opening: \(opening)"
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
