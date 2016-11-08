#!/usr/bin/env perl

use strict;

use File::Spec::Functions;

my @converts = (
    [ 'export_doap.xsl', 'doap' ],
    [ 'export_news.xsl', 'news' ],
    [ 'export_people.xsl', 'people' ],
    [ 'export_progress.xsl', 'progress' ],
    [ 'export_reports.xsl', 'reports' ],
);

opendir(my $dh, "..") || die "Unable to open directory\n$!";
while (my $f = readdir($dh)) {
    next if $f =~ /^\./;
    next unless $f =~ /(.*)\.xml/;
    my $pName = $1;
    my $iFn = catfile('..', $f);
    my $mFn = $pName.'.rdf';
    print "$iFn\n";
    my $links = '';
    foreach my $arr (@converts) {
         my $oFn = $pName.'_'.$arr->[1].'.rdf';
         my $cmd = "xsltproc $arr->[0] $iFn > $oFn";
         print "\t$cmd\n";
         `$cmd`;
         if ($? == 0) {
             $links .= "    <$arr->[1] rdf:resource=\"$oFn\" />\n";
         }
    }
    open(OUT, ">$mFn") || die "Unable to open '$mFn'\n$!";
    print OUT <<EOT;
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns="http://projects.apache.org/ns/asfext#">
  <incubatorProject rdf:about="$mFn">
$links  </incubatorProject>
</rdf:RDF>
EOT
    close(OOUT);
}

closedir($dh);
